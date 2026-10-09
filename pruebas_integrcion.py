from network_manager import NetworkManager

red = NetworkManager()
red.agregar_servidor("A")
red.agregar_servidor("B")
red.agregar_conexion("A", "B", 5)

auth_a = red.obtener_auth("A")
auth_a.registrar_usuario("Valeria", "1234")
assert auth_a.iniciar_sesion("Valeria", "1234") == True

fs_a = red.obtener_file_system("A")
fs_a.crear_carpeta("/", "docs")
fs_a.crear_archivo("/docs", "nota.txt")
assert fs_a.buscar_archivo("nota.txt") == ["/docs/nota.txt"]

fs_b = red.obtener_file_system("B")
assert fs_b.buscar_archivo("nota.txt") == []  # B no tiene lo de A

ruta, costo = red.enviar_paquete("A", "B")
assert ruta == ["A", "B"]
assert costo == 5

red.eliminar_servidor("A")
assert "A" not in red.sistemas_archivos
assert "A" not in red.autenticaciones

print("Pruebas de integración correctas.")
print("Revisar el network_audit_log.txt para ver los registros de auditoría.")