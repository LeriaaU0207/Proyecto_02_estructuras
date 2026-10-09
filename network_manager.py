from datetime import datetime
from grafo import Grafo
from file_system_manager import FileSystemManager
from auth_manager import AuthManager

class NetworkManager:
    def __init__(self, archivo_log="network_audit_log.txt"):
        self.grafo = Grafo()
        self.archivo_log = archivo_log
        self.sistemas_archivos = {}
        self.autenticaciones = {}

    def registrar_log(self, mensaje):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.archivo_log, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] [RED] {mensaje}\n")

    def agregar_servidor(self, nombre):
        archivos = FileSystemManager(nombre)
        auth = AuthManager(nombre)

        self.grafo.agregar_servidor(nombre)
        self.sistemas_archivos[nombre] = archivos
        self.autenticaciones[nombre] = auth

        self.registrar_log("Servidor agregado: " + nombre)


    def eliminar_servidor(self, nombre):
        self.grafo.eliminar_servidor(nombre)

        archivos = self.sistemas_archivos.get(nombre)
        if archivos is not None:
            archivos._limpiar_subarbol(archivos.raiz)
            del self.sistemas_archivos[nombre]

        if nombre in self.autenticaciones:    
            del self.autenticaciones[nombre]

        self.registrar_log(
            "Servidor eliminado con sus conexiones, archivos y usuarios: " + nombre
        )

    def agregar_conexion(self, origen, destino, latencia):
        self.grafo.agregar_conexion(origen, destino, latencia)
        self.registrar_log(f"Conexión agregada: {origen} <-> {destino}, {latencia} ms")

    def eliminar_conexion(self, origen, destino):
        self.grafo.eliminar_conexion(origen, destino)
        self.registrar_log(f"Conexión eliminada: {origen} <-> {destino}")

    def mostrar_red(self):
        if not self.grafo.adyacencia:
            print("No hay servidores registrados.")
            return
        for servidor, vecinos in self.grafo.adyacencia.items():
            conexiones = []
            for vecino, latencia in vecinos:
                conexiones.append(f"{vecino} ({latencia} ms)")
            if len(conexiones) == 0:
                texto = "sin conexiones"
            else:
                texto = ", ".join(conexiones)
            print(servidor + ": " + texto)

    def enviar_paquete(self, origen, destino, mostrar_pasos=False):
        ruta, costo, pasos = self.grafo.dijkstra(origen, destino)
        if mostrar_pasos:
            print("\nPasos de Dijkstra:")
            for paso in pasos:
                print(paso)

        if not ruta:
            print(f"No existe una ruta entre {origen} y {destino}.")
            self.registrar_log(f"Ruta calculada: {origen} -> {destino}; sin conexión")
            return ruta, costo

        print("\nRuta óptima: " + " -> ".join(ruta))
        acumulado = 0
        for i in range(len(ruta) - 1):
            latencia = self.grafo.obtener_latencia(ruta[i], ruta[i + 1])
            acumulado += latencia
            print(f"Salto {i + 1}: {ruta[i]} -> {ruta[i + 1]} | {latencia} ms | Acumulado: {acumulado} ms")
        if len(ruta) == 1:
            print("El origen y el destino son el mismo. No se necesitan saltos.")
        print(f"Costo total: {costo} ms")
        self.registrar_log(f"Ruta calculada: {' -> '.join(ruta)}; costo total: {costo} ms")
        return ruta, costo

    def ping_general(self, origen):
        alcanzables = self.grafo.bfs(origen)
        visitados = {}
        for servidor in alcanzables:
            visitados[servidor] = True
        no_alcanzables = []
        aislados = []
        for servidor, vecinos in self.grafo.adyacencia.items():
            if servidor not in visitados:
                no_alcanzables.append(servidor)
            if not vecinos:
                aislados.append(servidor)

        print("Recorrido BFS: " + " -> ".join(alcanzables))
        if no_alcanzables:
            print("No todos los servidores están comunicados.")
            print("No alcanzables desde " + origen + ": " + ", ".join(no_alcanzables))
        else:
            print("Todos los servidores son alcanzables desde " + origen + ".")
        texto_aislados = "ninguno"
        if len(aislados) > 0:
            texto_aislados = ", ".join(aislados)
        print("Servidores aislados (sin conexiones): " + texto_aislados)

        texto_no_alcanzables = "ninguno"
        if len(no_alcanzables) > 0:
            texto_no_alcanzables = ", ".join(no_alcanzables)
        self.registrar_log(
            f"Ping general desde {origen}; alcanzables: {', '.join(alcanzables)}; "
            f"no alcanzables: {texto_no_alcanzables}; "
            f"aislados: {texto_aislados}"
        )
        return alcanzables, no_alcanzables, aislados

    def mostrar_auditoria(self):
        try:
            with open(self.archivo_log, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            if contenido == "":
                print("La auditoría está vacía.")
            else:
                print(contenido)
        except FileNotFoundError:
            print("Todavía no hay registros de auditoría.")


    def obtener_file_system(self, nombre):
        if nombre not in self.sistemas_archivos:
            raise ValueError("No existe el servidor: " + nombre)

        return self.sistemas_archivos[nombre]

    def obtener_auth(self, nombre):
        if nombre not in self.autenticaciones:
            raise ValueError("No existe el servidor: " + nombre)

        return self.autenticaciones[nombre]