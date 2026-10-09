#==============================================================================
# Nodo
#==============================================================================
#Clase que representa un nodo de un árbol de directorios.

class Nodo:
    def __init__(self, nombre, tipo, padre=None):
        self.nombre = nombre
        self.tipo = tipo                # "Carpeta" o "archivo"
        self.padre = padre
        self.hijos = []                 # Solo las carpetas tienen hijos

    #busca un hijo por su nombre
    def buscar_hijo(self, nombre):
        """Busca unicamente entre los hijos director."""
        for hijo in self.hijos:
            if hijo.nombre == nombre:    #si coincide el nombre del hijo
                return hijo
        return None
    
    #crea un nodo
    def crear_nodo(self, nombre, tipo):
        #se valida el tipo
        if tipo not in ("carpeta", "archivo"):
            raise ValueError("El tipo debe ser 'carpeta' o 'archivo'")
        #si el nodo es un archivo, se debe estar en una carpeta
        if self.tipo != "carpeta":
            raise ValueError("No se puede crear un nodo dentro de un archivo")   
        #si el nombre del archivo no puede estar vacío o contener '/'
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        if "/" in nombre:
            raise ValueError("El nombre no puede contener '/'")
        #si ya existe un archivo con ese nombre
        if self.buscar_hijo(nombre) is not None:
            raise ValueError("Ya existe un nodo con ese nombre")

        #crea el nodo
        nuevo = Nodo(nombre, tipo, self)
        self.hijos.append(nuevo)
        return nuevo