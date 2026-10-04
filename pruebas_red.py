from network_manager import NetworkManager
from menu_red import cargar_ejemplo


def probar_red():
    red = NetworkManager()
    cargar_ejemplo(red)

    # assert detiene la prueba si el resultado no es el esperado
    print("\n1. Ruta más corta de A a D")
    ruta, costo = red.enviar_paquete("A", "D", True)
    assert ruta == ["A", "C", "B", "D"]
    assert costo == 4
    print("Correcto: la ruta cuesta 4 ms.")

    print("\n2. Ruta en sentido contrario")
    ruta, costo = red.enviar_paquete("D", "A")
    assert ruta == ["D", "B", "C", "A"]
    assert costo == 4
    print("Correcto: las conexiones funcionan en ambos sentidos.")

    print("\n3. Destino aislado")
    ruta, costo = red.enviar_paquete("A", "E")
    assert ruta == []
    assert costo == float("inf")
    print("Correcto: no existe una ruta hasta E.")

    print("\n4. Origen igual al destino")
    ruta, costo = red.enviar_paquete("E", "E")
    assert ruta == ["E"]
    assert costo == 0
    print("Correcto: no se necesitan saltos.")

    print("\n5. Ping general")
    alcanzables, no_alcanzables, aislados = red.ping_general("A")
    assert alcanzables == ["A", "B", "C", "D"]
    assert no_alcanzables == ["E"]
    assert aislados == ["E"]
    print("Correcto: E está aislado.")

    print("\n6. Eliminar una conexión cambia la ruta")
    red.eliminar_conexion("B", "D")
    ruta, costo = red.enviar_paquete("A", "D")
    assert ruta == ["A", "C", "D"]
    assert costo == 6
    print("Correcto: ahora el costo es 6 ms.")

    print("\n7. Eliminar un servidor elimina sus conexiones")
    red.eliminar_servidor("C")
    for vecinos in red.grafo.adyacencia.values():
        for vecino, latencia in vecinos:
            assert vecino != "C"
    ruta, costo = red.enviar_paquete("A", "D")
    assert ruta == []
    print("Correcto: ya no hay conexiones hacia C ni ruta hasta D.")

    print("\n8. Un grupo separado no es lo mismo que un servidor aislado")
    red.agregar_conexion("D", "E", 2)
    alcanzables, no_alcanzables, aislados = red.ping_general("A")
    assert alcanzables == ["A", "B"]
    assert no_alcanzables == ["D", "E"]
    assert aislados == []
    print("Correcto: D y E se conectan entre sí, pero no con A.")

    print("\n9. Conectar toda la red")
    red.agregar_conexion("B", "D", 1)
    alcanzables, no_alcanzables, aislados = red.ping_general("A")
    assert len(alcanzables) == 4
    assert no_alcanzables == []
    assert aislados == []
    print("Correcto: todos los servidores restantes se comunican.")

    print("\n10. Latencias cero y decimales")
    red.agregar_servidor("F")
    red.agregar_conexion("A", "F", 0)
    red.agregar_conexion("F", "E", 0.5)
    ruta, costo = red.enviar_paquete("A", "E")
    assert ruta == ["A", "F", "E"]
    assert costo == 0.5
    print("Correcto: se aceptan cero y decimales.")

    print("\n11. Rechazar latencias inválidas")
    for latencia in [-1, float("inf"), float("nan")]:
        hubo_error = False
        try:
            red.agregar_conexion("A", "D", latencia)
        except ValueError as error:
            hubo_error = True
            print("Error esperado:", error)
        assert hubo_error

    print("\n12. Rechazar un servidor inexistente")
    hubo_error = False
    try:
        red.enviar_paquete("A", "Z")
    except ValueError as error:
        hubo_error = True
        print("Error esperado:", error)
    assert hubo_error

    print("\nLas 12 pruebas terminaron correctamente.")
    print("Las operaciones realizadas se agregaron a network_audit_log.txt.")


if __name__ == "__main__":
    probar_red()
