from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo
from controllers.usuario import UsuarioController
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question,genera_codigo_by_texto
from datetime import datetime


class LibroController:
    def __init__(self):
        self.libro = Libro()
        self.usuario = Usuario()
        self.prestamo = Prestamo()
        self.usuario_controller = UsuarioController()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Libros
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_libros()
                elif respuesta == 2:
                    self.search_libro()
                elif respuesta == 3:
                    self.insert_libro()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_libros(self):
        try:
            print('''
            ==========================
                Listar Libros
            ==========================
            ''')
            libros = self.libro.get_libros('id_libro')
            print(print_table(libros, ['ID','Codigo', 'Titulo', 'Editorial', 'Stock']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_libro(self):
        print('''
        ========================
            Buscar Libro
        ========================
        ''')
        try:
            cod_libro = input_data("Ingrese el CODIGO del libro >> ")
            libro = self.libro.get_libro({
                'codigo': cod_libro
            })
            print(print_table(libro, ['ID','Codigo', 'Titulo', 'Editorial', 'Stock']))

            if libro:
                if question('¿Deseas dar mantenimiento, alquilar o devolver el libro?'):
                    opciones = ['Editar', 'Eliminar', 'Alquilar', 'Registrar Devolucion', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_libro(cod_libro)
                    elif respuesta == 2:
                        self.delete_libro(cod_libro)
                    elif respuesta == 3:
                        self.alquilar_libro(cod_libro)
                    elif respuesta == 4:
                        self.devolucion_libro(cod_libro)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')



    def devolucion_libro(self, cod_libro):

      #Obtiene Libro
      libro = self.libro.get_libro({
          'codigo': cod_libro
      })

      self.usuario_controller.all_usuarios()

      while True:
        codigo = input_data('Ingrese el Codigo del Usuario que Alquilo el libro >> ')
        
        #Obtiene User
        user = self.usuario.get_usuario({
            'codigo': codigo
        })

        if user:
            prestamos = self.prestamo.get_prestamo({
                'id_usuario': user[0],
                'id_libro': libro[0],
                'devuelto': False
            })

            print('''
            ======================================
                Lista de Prestamos del Usuario
            ======================================
            ''')

            print(print_table(prestamos, ['ID Prestamo','ID Libro', 'ID Usuario', 'Fecha Prestamo', 'Fecha Devolucion', 'Devuelto']))
            input('\nPresiona una tecla para continuar...')

            while True:
                id_prestamo = input_data('Ingrese el Id del Prestamo que desea registrar la devolucion >> ', 'int')

                prest = self.prestamo.get_prestamo({
                    'id_prestamo': id_prestamo
                })

                if prest:
                    now = datetime.now()
                    fecha_devolucion = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

                    self.prestamo.update_prestamo({
                        'id_prestamo': id_prestamo
                    }, {
                        'fecha_devolucion': fecha_devolucion,
                        'devuelto': True

                    })

                    self.update_stock_of_devolucion_libro_by_codlibro(cod_libro)
            
                    print(f'''
                    ==========================================================================
                        Libro {libro[2]} Devuelto por {user[4]} {user[5]} {user[6]} con Exito
                    ==========================================================================
                    ''')
                    prestamos_2 = self.prestamo.get_prestamo({
                        'id_usuario': user[0],
                        'id_libro': libro[0],
                    })

                    print(print_table(prestamos_2, ['ID Prestamo','ID Libro', 'ID Usuario', 'Fecha Prestamo', 'Fecha Devolucion', 'Devuelto']))

                    break
            break


    def alquilar_libro(self, cod_libro):

        if (self.valida_disponibilidad_by_codlibro(cod_libro)):

          print (f'\n Libro Disponible para Alquiler \n')

          #Obtiene Libro
          libro = self.libro.get_libro({
              'codigo': cod_libro
          })

          self.usuario_controller.all_usuarios()
          while True:
            codigo = input_data('Ingrese el Codigo de uno de los Usuario que Alquilara del libro >> ')

            #Obtiene User
            user = self.usuario.get_usuario({
                'codigo': codigo
            })

            if user:
              now = datetime.now()
              fecha_prestamo = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

              self.prestamo.insert_prestamo({
                  'id_usuario': user[0],
                  'id_libro': libro[0],
                  'fecha_prestamo': fecha_prestamo,
                  'devuelto': False
              })

              self.update_stock_of_alquiler_libro_by_codlibro(cod_libro)
              
              print(f'''
              ==========================================================================
                  Libro {libro[2]} alquilado a {user[4]} {user[5]} {user[6]} con Exito
              ==========================================================================
              ''')
              break
        else:
          print('''
          ================================
              Libro sin Stock
          ================================
          ''')

    def insert_libro(self):
        titulo = input_data('Ingrese el titulo del libro >> ')
        editorial = input_data('Ingrese la editorial del libro >> ')
        stock = input_data('Ingrese el Stock del libro >> ', 'int')
        codigo = genera_codigo_by_texto(titulo)
        self.libro.insert_libro({
            'codigo': codigo,
            'titulo': titulo,
            'editorial': editorial,
            'stock': stock
        })
        print('''
        ================================
            Nuevo libro agregado
        ================================
        ''')
        self.all_libros()

    def update_libro(self, cod_libro):
        titulo = input_data('Ingrese el Nuevo titulo del libro >> ')
        editorial = input_data('Ingrese la Nueva editorial del libro >> ')
        stock = input_data('Ingrese el nuevo Stock del libro >> ', 'int')
        self.libro.update_libro({
            'codigo': cod_libro
        }, {
            'titulo': titulo,
            'editorial': editorial,
            'stock': stock
        })
        print('''
        ============================
            Libro Actualizado
        ============================
        ''')

    def delete_libro(self, cod_libro):
        self.libro.delete_libro({
            'codigo': cod_libro
        })
        print('''
        =========================
            Libro Eliminado
        =========================
        ''')


    def update_stock_by_codlibro(self, cod_libro, stock):
        self.libro.update_libro({
            'codigo': cod_libro
        }, {
            'stock': stock
        })
        return True

    def obtiene_stock_by_codlibro(self, cod_libro):

        libro = self.libro.get_libro({
            'codigo': cod_libro
        })

        if libro:
          return libro[4]

        return 0

    def valida_disponibilidad_by_codlibro(self, cod_libro):

        stock = int(self.obtiene_stock_by_codlibro(cod_libro))
          
        if stock > 0:
          return True
        
        return False

    def update_stock_of_alquiler_libro_by_codlibro(self, cod_libro):

        if self.valida_disponibilidad_by_codlibro(cod_libro):
          stock = int(self.obtiene_stock_by_codlibro(cod_libro))
          self.update_stock_by_codlibro(cod_libro, stock - 1)
          return True

        return False

    def update_stock_of_devolucion_libro_by_codlibro(self, cod_libro):

        stock = int(self.obtiene_stock_by_codlibro(cod_libro))
        self.update_stock_by_codlibro(cod_libro, stock + 1)
        return True


