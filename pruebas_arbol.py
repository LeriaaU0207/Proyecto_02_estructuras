#==============================================================================
# Pruebas de la clase FileSystemManager
#==============================================================================     
#Archivo que contiene las pruebas de la clase FileSystemManager
#Este se creo para poder ejecutar los tests desde la consola de manere temporal 
"""
from file_system_manager import FileSystemManager

#definición de la función para preparar el sistema
def preparar_sistema():
    sistema = FileSystemManager()
    #se crean los nodos del árbol de directorios con carpetas y archivos
    sistema.crear_carpeta("/", "documentos")
    sistema.crear_carpeta("/documentos", "tareas")
    sistema.crear_archivo("/documentos/tareas", "avance.txt")
    sistema.crear_carpeta("/", "respaldos")
    sistema.crear_archivo("/respaldos", "copia.txt")
    sistema.mostrar_arbol()  # Muestra el árbol inicial
    return sistema


# PRUEBA 1: Impedir el borrado de la raíz
print("\n=== PRUEBA 1: ELIMINAR LA RAÍZ ===")
sistema = preparar_sistema()
try:
    sistema.eliminar("/")
    print("ERROR: permitió eliminar la raíz")
except ValueError as error:
    print(f"Correcto, se rechazó la operación: {error}")

sistema.mostrar_arbol()  # Debe seguir completo.


# PRUEBA 2: Eliminar únicamente un archivo
print("\n=== PRUEBA 2: ELIMINAR UN ARCHIVO ===")
sistema = preparar_sistema()
sistema.eliminar("/documentos/tareas/avance.txt")
sistema.mostrar_arbol()
# Deben permanecer documentos/, tareas/ y respaldos/.


# PRUEBA 3: Eliminar una carpeta con descendientes
print("\n=== PRUEBA 3: BORRADO EN CASCADA ===")
sistema = preparar_sistema()
print("Antes:")
sistema.mostrar_arbol()

sistema.eliminar("/documentos")

print("Después:")
sistema.mostrar_arbol()
# Debe quedar únicamente respaldos/ con copia.txt.


# PRUEBA 4: Eliminar una ruta que no existe
print("\n=== PRUEBA 4: RUTA INEXISTENTE ===")
sistema = preparar_sistema()
try:
    sistema.eliminar("/carpeta_inexistente")
    print("ERROR: permitió eliminar una ruta inexistente")
except ValueError as error:
    print(f"Correcto, se rechazó la operación: {error}")

sistema.mostrar_arbol()  # No debe haber cambiado.
"""