class Grafo:
    def __init__(self):
        # Cada servidor guarda una lista de vecinos y sus latencias
        self.adyacencia = {}

    def validar_servidor(self, nombre):
        if nombre not in self.adyacencia:
            raise ValueError("No existe el servidor: " + str(nombre))

    def agregar_servidor(self, nombre):
        if type(nombre) != str or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if nombre != nombre.strip() or not nombre.isprintable():
            raise ValueError("El nombre no debe tener saltos ni espacios en los extremos.")
        if nombre in self.adyacencia:
            raise ValueError("Ya existe ese servidor.")
        self.adyacencia[nombre] = []

    def eliminar_servidor(self, nombre):
        self.validar_servidor(nombre)
        for vecino, latencia in self.adyacencia[nombre]:
            self.adyacencia[vecino].remove((nombre, latencia))
        del self.adyacencia[nombre]

    def agregar_conexion(self, origen, destino, latencia):
        self.validar_servidor(origen)
        self.validar_servidor(destino)
        if origen == destino:
            raise ValueError("Una conexión debe unir dos servidores diferentes.")
        if type(latencia) != int and type(latencia) != float:
            raise ValueError("La latencia debe ser un número.")
        # El peso debe estar entre cero e infinito, sin incluir infinito
        if not (0 <= latencia < float("inf")):
            raise ValueError("La latencia debe ser finita y mayor o igual a cero.")
        for vecino, peso in self.adyacencia[origen]:
            if vecino == destino:
                raise ValueError("Esa conexión ya existe. Elimínela antes de cambiarla.")

        # La conexión funciona en ambos sentidos
        self.adyacencia[origen].append((destino, latencia))
        self.adyacencia[destino].append((origen, latencia))

    def eliminar_conexion(self, origen, destino):
        self.validar_servidor(origen)
        self.validar_servidor(destino)
        for vecino, latencia in self.adyacencia[origen]:
            if vecino == destino:
                self.adyacencia[origen].remove((destino, latencia))
                self.adyacencia[destino].remove((origen, latencia))
                return
        raise ValueError("No existe esa conexión.")

    def obtener_latencia(self, origen, destino):
        self.validar_servidor(origen)
        self.validar_servidor(destino)
        for vecino, latencia in self.adyacencia[origen]:
            if vecino == destino:
                return latencia
        raise ValueError("No existe esa conexión.")

    def dijkstra(self, origen, destino):
        self.validar_servidor(origen)
        self.validar_servidor(destino)
        distancias = {}
        anteriores = {}
        visitados = {}
        pasos = []

        for servidor in self.adyacencia:
            distancias[servidor] = float("inf")
            anteriores[servidor] = None
            visitados[servidor] = False
        distancias[origen] = 0

        while True:
            actual = None
            menor_distancia = float("inf")

            # Busca el pendiente que tiene el menor costo acumulado
            for servidor in self.adyacencia:
                if visitados[servidor] == False and distancias[servidor] < menor_distancia:
                    actual = servidor
                    menor_distancia = distancias[servidor]

            if actual is None:
                break

            visitados[actual] = True
            pasos.append(f"Se fija {actual} con costo {distancias[actual]} ms.")
            if actual == destino:
                break

            for vecino, latencia in self.adyacencia[actual]:
                if visitados[vecino] == False:
                    nuevo_costo = distancias[actual] + latencia
                    if nuevo_costo < distancias[vecino]:
                        distancias[vecino] = nuevo_costo
                        anteriores[vecino] = actual
                        pasos.append(f"Se mejora {vecino}: {nuevo_costo} ms pasando por {actual}.")

        if distancias[destino] == float("inf"):
            pasos.append("No hay una ruta hacia el destino.")
            return [], float("inf"), pasos

        # Recupera la ruta desde el destino hacia el origen
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]
        ruta.reverse()
        return ruta, distancias[destino], pasos

    def bfs(self, origen):
        self.validar_servidor(origen)
        cola = [origen]
        visitados = {}
        for servidor in self.adyacencia:
            visitados[servidor] = False
        visitados[origen] = True
        recorrido = []
        posicion = 0

        # El índice permite usar la lista como una cola FIFO
        while posicion < len(cola):
            actual = cola[posicion]
            posicion += 1
            recorrido.append(actual)

            for vecino, latencia in self.adyacencia[actual]:
                if visitados[vecino] == False:
                    visitados[vecino] = True
                    cola.append(vecino)
        return recorrido
