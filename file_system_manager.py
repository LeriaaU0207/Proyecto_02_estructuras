import os
from nodo import Nodo
#==============================================================================
# FileSystemManager
#==============================================================================
#Clase que representa un árbol de directorios.

class FileSystemManager:
    def __init__(self):
        self.raiz = Nodo("/", "carpeta")

    #busca un nodo por su ruta
    def _buscar_por_ruta(self,ruta):
        """sigue cada parte de la ruta desde la raíz."""
        if ruta == "/":                     #si es la raíz
            return self.raiz
        if not ruta.startswith("/"):        #si no empieza con /
            raise ValueError("La ruta debe comenzar con '/'")  
            return None
        
        partes = [parte for parte in ruta.split("/") if parte]  #separa las partes de la ruta
        actual = self.raiz
        for parte in partes:                                    #busca cada parte de la ruta
            actual = actual.buscar_hijo(parte)                  #si no existe, devuelve None    
            if actual is None:
                return None
        return actual                                           #si existe, devuelve el nodo   

    #crea una carpeta dentro de una carpeta
    def crear_carpeta(self, ruta_padre, nombre):
        padre = self._buscar_por_ruta(ruta_padre)               #busca el padre
        if padre is None:
            raise Exception("Ruta no encontrada")                #si no existe, devuelve None   

        return padre.crear_nodo(nombre, "carpeta")               #crea el nodo y devuelve el padre
    
    #crea un archivo dentro de una carpeta
    def crear_archivo(self, ruta_padre, nombre):
        padre = self._buscar_por_ruta(ruta_padre)                
        if padre is None:
            raise Exception("Ruta no encontrada")
        
        return padre.crear_nodo(nombre, "archivo")               #crea el nodo y devuelve el padre  

    #busca archivos por nombre
    def buscar_archivo(self, nombre):
        """Devyelve las rutas de los archivos que coincidan con el nombre dado."""
        resultado = []                                         #guarda las rutas de los archivos
        def recorrer(nodo, ruta_actual):
            if nodo.tipo == "archivo" and nodo.nombre == nombre:    #si es un archivo y coincide el nombre 
                resultado.append(ruta_actual)                      #lo guarda en la lista

            for hijo in nodo.hijos:                               
                if ruta_actual == "/":
                    ruta_hijo = "/" + hijo.nombre                   #si es la raíz, se agrega / al principio
                else:
                    ruta_hijo = ruta_actual + "/" + hijo.nombre
                recorrer(hijo, ruta_hijo)
        recorrer(self.raiz, "/")
        return resultado

    #imprime el árbol
    def mostrar_arbol(self):
        def mostrar(nodo, profundidad):                          #función recursiva para mostrar el árbol   
            sangria = " " * profundidad                          #sangría para indentar el árbol
            nombre = nodo.nombre                                #nombre del nodo

            if nodo.tipo == "carpeta" and nodo is not self.raiz:    #si es una carpeta y no es la raíz
                nombre += "/"                                    #se agrega / al final
                print(sangria + nombre)                          #imprime el nombre del nodo

                for hijo in nodo.hijos:
                    mostrar(hijo, profundidad + 1)               #llama a la función recursiva para imprimir el árbol
        mostrar(self.raiz, 0)

    #limpia el árbol de los hijos
    def _limpiar_subarbol(self, nodo):
        """Recorre primero descendientes y despues limpia el nodo."""
        for hijo in nodo.hijos:
            self._limpiar_subarbol(hijo)                         #llama a la función recursiva para limpiar el árbol    

        nodo.hijos.clear()                                      #limpia los hijos del nodo  
        nodo.padre = None                                       #limpia el padre del nodo   

    #elimina un nodo del árbol
    def eliminar(self, ruta):
        if ruta == "/":                                         #si es la raíz
            raise ValueError("No se puede eliminar la raíz")     #se lanza una excepción
        
        nodo = self._buscar_por_ruta(ruta)                      #busca el nodo
        if nodo is None:
            raise ValueError("Ruta no encontrada")

        padre = nodo.padre                                      #busca el padre
        if padre is None:
            raise ValueError("No se puede eliminar la raíz")
        padre.hijos.remove(nodo)
        self._limpiar_subarbol(nodo)                             #limpia el árbol
        return True
