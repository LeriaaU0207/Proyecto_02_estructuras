import os
from network_manager import NetworkManager
from menu_red import menu_red


def menu_archivos(red, servidor):
    archivos = red.obtener_file_system(servidor)

    while True:
        print("\n--- ARCHIVOS DEL SERVIDOR", servidor, "---")
        print("1. Crear carpeta")
        print("2. Crear archivo")
        print("3. Buscar archivo")
        print("4. Mostrar árbol")
        print("5. Eliminar archivo o carpeta")
        print("0. Volver")

        opcion = input("Opción: ").strip()

        try:
            if opcion == "1" or opcion == "2":
                ruta = input("Ruta de la carpeta padre, por ejemplo /: ").strip()
                nombre = input("Nombre: ").strip()

                if opcion == "1":
                    archivos.crear_carpeta(ruta, nombre)
                else:
                    archivos.crear_archivo(ruta, nombre)

                print("Creado correctamente.")

            elif opcion == "3":
                nombre = input("Nombre del archivo: ").strip()
                resultados = archivos.buscar_archivo(nombre)

                if not resultados:
                    print("No se encontró el archivo.")
                else:
                    for ruta in resultados:
                        print(ruta)

            elif opcion == "4":
                archivos.mostrar_arbol()

            elif opcion == "5":
                ruta = input("Ruta que desea eliminar: ").strip()
                respuesta = input(
                    "¿Eliminar también todo su contenido? (s/n): "
                ).strip().lower()

                if respuesta == "s":
                    archivos.eliminar(ruta)
                    print("Eliminado correctamente.")

            elif opcion == "0":
                return

            else:
                print("Opción inválida.")

        except OSError as error:
            print("No se pudo guardar la auditoría:", error)
            print("Revise el árbol: el cambio pudo haberse aplicado.")

        except Exception as error:
            print("No se pudo completar la operación:", error)


def menu_sesion(red, servidor, usuario):
    auth = red.obtener_auth(servidor)

    while True:
        print("\n--- SESIÓN ---")
        print("Servidor:", servidor)
        print("Usuario:", usuario)
        print("1. Administrar archivos")
        print("2. Mostrar tabla hash de usuarios")
        print("3. Eliminar mi usuario")
        print("0. Cerrar sesión")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_archivos(red, servidor)

        elif opcion == "2":
            auth.mostrar_tabla()

        elif opcion == "3":
            respuesta = input(
                "¿Seguro que desea eliminar su usuario? (s/n): "
            ).strip().lower()

            if respuesta == "s":
                if auth.eliminar_usuario(usuario):
                    print("Usuario eliminado. Sesión cerrada.")
                    return
                else:
                    print("No se pudo eliminar el usuario.")

        elif opcion == "0":
            auth.registrar_log(
                "Cierre de sesión en " + servidor + ": " + usuario
            )
            print("Sesión cerrada.")
            return

        else:
            print("Opción inválida.")


def entrar_servidor(red):
    servidor = input("Nombre del servidor: ").strip()
    auth = red.obtener_auth(servidor)

    while True:
        print("\n--- ACCESO AL SERVIDOR", servidor, "---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("0. Volver")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            return

        if opcion != "1" and opcion != "2":
            print("Opción inválida.")
            continue

        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ")

        if not usuario or not contrasena.strip():
            print("El usuario y la contraseña no pueden estar vacíos.")
            continue

        if opcion == "1":
            if auth.registrar_usuario(usuario, contrasena):
                print("Usuario registrado. Ahora puede iniciar sesión.")
            else:
                print("Ese usuario ya existe en este servidor.")

        elif opcion == "2":
            if auth.iniciar_sesion(usuario, contrasena):
                print("Inicio de sesión correcto.")
                menu_sesion(red, servidor, usuario)
            else:
                print("Usuario o contraseña incorrectos.")


def main():
    carpeta_proyecto = os.path.dirname(os.path.abspath(__file__))
    os.chdir(carpeta_proyecto)

    red = NetworkManager()

    print("Los datos simulados duran mientras el programa esté abierto.")
    print("La auditoría sí se conserva en el archivo de texto.")

    while True:
        print("\n--- SISTEMA OPERATIVO DE RED ---")
        print("1. Administrar red, rutas y ping")
        print("2. Entrar a un servidor")
        print("3. Ver auditoría")
        print("0. Salir")

        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                menu_red(red)

            elif opcion == "2":
                entrar_servidor(red)

            elif opcion == "3":
                red.mostrar_auditoria()

            elif opcion == "0":
                print("Programa terminado.")
                return

            else:
                print("Opción inválida.")

        except ValueError as error:
            print("Error:", error)

        except OSError as error:
            print("No se pudo acceder a la auditoría:", error)
            print("La operación pudo aplicarse. Revise el estado del sistema.")


if __name__ == "__main__":
    main()