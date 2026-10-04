class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def obtener_nombre_usuario(self):
        return self.nombre_usuario

    def verificar_contrasena(self, contrasena):
        return self.contrasena == contrasena

    def __str__(self):
        return self.nombre_usuario