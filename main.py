from helpers.menu import Menu
from controllers.usuario import UsuarioController
from controllers.libro import LibroController

def app():
    try:
        print('''
        ==========================
            Biblioteca Virtual
        ==========================
        ''')
        menu_principal = ["Usuarios","Libros", "Salir"]
        respuesta = Menu(menu_principal).show()
        print(respuesta)
        if respuesta == 1:
            usuario = UsuarioController()
            usuario.menu()
            if usuario.salir:
                app()
        elif respuesta == 2:
            libro = LibroController()
            libro.menu()
            if libro.salir:
                app()
  
        print("\n Gracias por utilizar el sistema \n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

app()