import queue

class Vertice:
    def __init__(self, id):
        self.id = id
        self.conexiones = {}
        self.distancia = float('inf')
        self.predecesor = None

    def agregarVecino(self, vecino, ponderacion=0):
        self.conexiones[vecino] = ponderacion

    def obtenerConexiones(self):
        return self.conexiones.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conexiones[vecino]

    def asignarDistancia(self, dist):
        self.distancia = dist

    def obtenerDistancia(self):
        return self.distancia

    def asignarPredecesor(self, pred):
        self.predecesor = pred

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        vertice = Vertice(id)
        self.vertices[id] = vertice
        return vertice

    def agregarArista(self, de, a, costo=0):
        if de not in self.vertices:
            self.agregarVertice(de)
        if a not in self.vertices:
            self.agregarVertice(a)
        self.vertices[de].agregarVecino(self.vertices[a], costo)

    def __iter__(self):
        return iter(self.vertices.values())

def dijkstra(grafo, inicio):
    inicio.asignarDistancia(0)
    cola_prioridad = queue.PriorityQueue()
    cola_prioridad.put((inicio.obtenerDistancia(), inicio))

    while not cola_prioridad.empty():
        distancia_actual, vertice_actual = cola_prioridad.get()

        for vecino in vertice_actual.obtenerConexiones():
            nueva_distancia = distancia_actual + vertice_actual.obtenerPonderacion(vecino)

            if nueva_distancia < vecino.obtenerDistancia():
                vecino.asignarDistancia(nueva_distancia)
                vecino.asignarPredecesor(vertice_actual)
                cola_prioridad.put((nueva_distancia, vecino))

# Ejemplo de uso:
grafo = Grafo()
grafo.agregarArista('A', 'B', 1)
grafo.agregarArista('A', 'C', 4)
grafo.agregarArista('B', 'C', 2)
grafo.agregarArista('B', 'D', 5)
grafo.agregarArista('C', 'D', 1)

dijkstra(grafo, grafo.vertices['A'])

# Mostrar la distancia mínima desde 'A' a cada vértice
for vertice in grafo:
    print(f"Distancia desde A a {vertice.obtenerId()} es {vertice.obtenerDistancia()}")
