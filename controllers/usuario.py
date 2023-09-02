from models.usuario import Usuario
from helpers.menu import Menu
from helpers.helper import input_data, print_table, question, genera_codigo_by_texto


class UsuarioController:
    def __init__(self):
        self.usuario = Usuario()
        self.salir = False

    def menu(self):
        try:
            while True:
                print('''
                ==================
                    Usuarios
                ==================
                ''')
                lista_menu = ["Listar", "Buscar", "Crear", "Salir"]
                respuesta = Menu(lista_menu).show()

                if respuesta == 1:
                    self.all_usuarios()
                elif respuesta == 2:
                    self.search_usuario()
                elif respuesta == 3:
                    self.insert_usuario()
                else:
                    self.salir = True
                    break
        except Exception as e:
            print(f'{str(e)}')

    def all_usuarios(self):
        try:
            print('''
            ==========================
                Listar Usuarios
            ==========================
            ''')
            usuarios = self.usuario.get_usuarios('id_usuario')
            print(print_table(usuarios, ['ID', 'Tipo Doc', 'Num Doc', 'Codigo', 'Nombre', 'Ap. Paterno', 'Ap. Materno']))
            input('\nPresiona una tecla para continuar...')
        except Exception as e:
            print(f'{str(e)}')

    def search_usuario(self):
        print('''
        ========================
            Buscar Usuario
        ========================
        ''')
        try:
            cod_usuario = input_data("Ingrese el Codigo del usuario >> ")
            usuario = self.usuario.get_usuario({
                'codigo': cod_usuario
            })
            print(print_table(usuario, ['ID', 'Tipo Doc', 'Num Doc', 'Codigo', 'Nombre', 'Ap. Paterno', 'Ap. Materno']))

            if usuario:
                if question('¿Deseas dar mantenimiento al usuario?'):
                    opciones = ['Editar', 'Eliminar', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.update_usuario(cod_usuario)
                    elif respuesta == 2:
                        self.delete_usuario(cod_usuario)
        except Exception as e:
            print(f'{str(e)}')
        input('\nPresiona una tecla para continuar...')

    def insert_usuario(self):
        print('Seleccion el Tipo de Documento del usuario >>')
        lista_menu = ["DNI", "RUC", "PASAPORTE", "OTRO"]
        respuesta = Menu(lista_menu).show()
        if respuesta == 1:
            tipo_doc='DNI'
        elif respuesta == 2:
            tipo_doc='RUC'
        elif respuesta == 3:
            tipo_doc='PASAPORTE'
        else:
            tipo_doc='OTRO'

        num_doc = input_data('Ingrese el Numero Documento del usuario >> ')
        nombre = input_data('Ingrese el Nombre del usuario >> ')
        ap_paterno = input_data('Ingrese el Apellido Paterno del usuario >> ')
        ap_materno = input_data('Ingrese el Apellido Materno del usuario >> ')
        codigo = genera_codigo_by_texto(ap_paterno + ap_materno)

        self.usuario.insert_usuario({
            'tipo_doc': tipo_doc,
            'num_doc': num_doc,
            'codigo': codigo,
            'nombre': nombre,
            'ap_paterno': ap_paterno,
            'ap_materno': ap_materno
        })
        print('''
        ================================
            Nuevo usuario agregado
        ================================
        ''')
        self.all_usuarios()

    def update_usuario(self, cod_usuario):
        
        print('Seleccion el Nuevo Tipo de Documento del usuario >>')
        lista_menu = ["DNI", "RUC", "PASAPORTE", "OTRO"]
        respuesta = Menu(lista_menu).show()
        if respuesta == 1:
            tipo_doc='DNI'
        elif respuesta == 2:
            tipo_doc='RUC'
        elif respuesta == 3:
            tipo_doc='PASAPORTE'
        else:
            tipo_doc='OTRO'

        num_doc = input_data('Ingrese el Nuevo Numero Documento del usuario >> ')
        nombre = input_data('Ingrese el Nuevo Nombre del usuario >> ')
        ap_paterno = input_data('Ingrese el Nuevo Apellido Paterno del usuario >> ')
        ap_materno = input_data('Ingrese el Nuevo Apellido Materno del usuario >> ')
        self.usuario.update_usuario({
            'codigo': cod_usuario
        }, {
            'tipo_doc': tipo_doc,
            'num_doc': num_doc,
            'nombre': nombre,
            'ap_paterno': ap_paterno,
            'ap_materno': ap_materno
        })
        print('''
        ============================
            Usuario Actualizado
        ============================
        ''')

    def delete_usuario(self, cod_usuario):
        self.usuario.delete_usuario({
            'codigo': cod_usuario
        })
        print('''
        =========================
            Usuario Eliminado
        =========================
        ''')

