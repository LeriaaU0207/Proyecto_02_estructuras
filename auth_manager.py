from tabla_hash import TablaHash
from datetime import datetime


class AuthManager:
    def __init__(self, nombre_servidor="local"):
        self.tabla_usuarios = TablaHash()
        self.nombre_servidor = nombre_servidor

    # Guarda las acciones importantes en el archivo de auditoria
    def registrar_log(self, mensaje):
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(
            "network_audit_log.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
            f"[{fecha_hora}] [AUTH] Usuario {self.nombre_servidor}: {mensaje}\n"
            )

    # Registra un nuevo usuario
    def registrar_usuario(self, nombre_usuario, contrasena):
        resultado = self.tabla_usuarios.insertar(
            nombre_usuario,
            contrasena
        )

        if resultado:
            self.registrar_log(
                "Usuario registrado: " + nombre_usuario
            )
            return True

        self.registrar_log(
            "Intento de registrar usuario existente: " + nombre_usuario
        )

        return False


    # Verifica el usuario y la contrasena para iniciar sesion
    def iniciar_sesion(self, nombre_usuario, contrasena):
        resultado = self.tabla_usuarios.autenticar(
            nombre_usuario,
            contrasena
        )

        if resultado:
            self.registrar_log(
                "Inicio de sesion exitoso: " + nombre_usuario
            )
            return True

        self.registrar_log(
            "Inicio de sesion fallido: " + nombre_usuario
        )

        return False


    # Elimina un usuario existente
    def eliminar_usuario(self, nombre_usuario):
        resultado = self.tabla_usuarios.eliminar(nombre_usuario)

        if resultado:
            self.registrar_log(
                "Usuario eliminado: " + nombre_usuario
            )
            return True

        self.registrar_log(
            "Intento de eliminar usuario inexistente: " + nombre_usuario
        )

        return False


    # Busca un usuario
    def buscar_usuario(self, nombre_usuario):
        return self.tabla_usuarios.buscar(nombre_usuario)


    # Muestra la tabla hash
    def mostrar_tabla(self):
        self.tabla_usuarios.mostrar_tabla()
