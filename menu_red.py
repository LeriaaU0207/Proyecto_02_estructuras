from network_manager import NetworkManager


def cargar_ejemplo(red):
    if red.grafo.adyacencia:
        raise ValueError("El ejemplo solo se puede cargar en una red vacía.")
    for nombre in ["A", "B", "C", "D", "E"]:
        red.agregar_servidor(nombre)
    red.agregar_conexion("A", "B", 4)
    red.agregar_conexion("A", "C", 1)
    red.agregar_conexion("C", "B", 2)
    red.agregar_conexion("B", "D", 1)
    red.agregar_conexion("C", "D", 5)
    print("Ejemplo cargado. E está aislado. La mejor ruta de A a D cuesta 4 ms.")


def menu_red(red):
    while True:
        print("\n--- RED DE SERVIDORES ---")
        print("1. Agregar servidor")
        print("2. Eliminar servidor")
        print("3. Agregar conexión")
        print("4. Eliminar conexión")
        print("5. Mostrar red")
        print("6. Enviar paquete con Dijkstra")
        print("7. Ping general con BFS")
        print("8. Ver auditoría")
        print("9. Cargar ejemplo")
        print("0. Volver o salir")
        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                red.agregar_servidor(input("Nombre del servidor: ").strip())
                print("Servidor agregado.")
            elif opcion == "2":
                red.eliminar_servidor(input("Servidor que desea eliminar: ").strip())
                print("Servidor eliminado.")
            elif opcion == "3":
                origen = input("Servidor origen: ").strip()
                destino = input("Servidor destino: ").strip()
                latencia = float(input("Latencia en ms: "))
                red.agregar_conexion(origen, destino, latencia)
                print("Conexión agregada.")
            elif opcion == "4":
                origen = input("Servidor origen: ").strip()
                destino = input("Servidor destino: ").strip()
                red.eliminar_conexion(origen, destino)
                print("Conexión eliminada.")
            elif opcion == "5":
                red.mostrar_red()
            elif opcion == "6":
                origen = input("Servidor origen: ").strip()
                destino = input("Servidor destino: ").strip()
                respuesta = input("¿Ver los pasos de Dijkstra? (s/n): ").strip().lower()
                red.enviar_paquete(origen, destino, respuesta == "s")
            elif opcion == "7":
                red.ping_general(input("Servidor desde el que inicia el ping: ").strip())
            elif opcion == "8":
                red.mostrar_auditoria()
            elif opcion == "9":
                cargar_ejemplo(red)
            elif opcion == "0":
                return
            else:
                print("Opción inválida.")
        except ValueError as error:
            print("Error:", error)
        except OSError as error:
            print("No se pudo acceder a la auditoría:", error)
            print("Si estaba modificando la red, revise su estado: el cambio pudo aplicarse.")


if __name__ == "__main__":
    red = NetworkManager()
    menu_red(red)
