from usuario import Usuario

class NodoHash:
    def __init__(self, usuario):
        self.usuario = usuario
        self.siguiente = None


class TablaHash:
    def __init__(self, tamano=10):
        self.tamano = tamano
        self.tabla = [None] * tamano

    # Convierte el nombre de usuario en un indice de la tabla
    def funcion_hash(self, nombre_usuario):
        valor_hash = 0

        for caracter in nombre_usuario:
            valor_hash = (valor_hash * 31 + ord(caracter)) % self.tamano

        return valor_hash

    # Inserta un usuario en la tabla hash
    def insertar(self, nombre_usuario, contrasena):
        indice = self.funcion_hash(nombre_usuario)

        # Primero revisamos si el usuario ya existe
        actual = self.tabla[indice]

        while actual is not None:
            if actual.usuario.obtener_nombre_usuario() == nombre_usuario:
                return False

            actual = actual.siguiente

        # Creamos el usuario usando la clase Usuario
        nuevo_usuario = Usuario(nombre_usuario, contrasena)

        # Creamos el nodo que guardara al usuario
        nuevo_nodo = NodoHash(nuevo_usuario)

        # Lo colocamos al inicio de la lista de ese indice
        nuevo_nodo.siguiente = self.tabla[indice]
        self.tabla[indice] = nuevo_nodo

        return True

    # Busca un usuario en la tabla hash
    def buscar(self, nombre_usuario):
        indice = self.funcion_hash(nombre_usuario)
        actual = self.tabla[indice]

        while actual is not None:
            if actual.usuario.obtener_nombre_usuario() == nombre_usuario:
                return actual.usuario

            actual = actual.siguiente

        return None

    # Elimina un usuario de la tabla hash
    def eliminar(self, nombre_usuario):
        indice = self.funcion_hash(nombre_usuario)

        actual = self.tabla[indice]
        anterior = None

        while actual is not None:
            if actual.usuario.obtener_nombre_usuario() == nombre_usuario:

                # Si es el primer nodo de la lista
                if anterior is None:
                    self.tabla[indice] = actual.siguiente

                # Si esta en medio o al final
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False

    # Permite verificar una contrasena
    def autenticar(self, nombre_usuario, contrasena):
        usuario = self.buscar(nombre_usuario)

        if usuario is None:
            return False

        return usuario.verificar_contrasena(contrasena)

    # Muestra el contenido de la tabla hash
    # Util para pruebas y para explicar colisiones
    def mostrar_tabla(self):
        for indice in range(self.tamano):

            print(str(indice) + ":", end=" ")

            actual = self.tabla[indice]

            if actual is None:
                print("Vacio")

            else:
                while actual is not None:
                    print(
                        actual.usuario.obtener_nombre_usuario(),
                        end=" -> "
                    )

                    actual = actual.siguiente

                print("None")