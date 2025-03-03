import heapq  # Importamos el módulo heapq para utilizar una cola de prioridad eficiente

def dijkstra_with_paths(graph, start):
    # Inicializamos el diccionario de distancias con infinito para todos los nodos
    distances = {vertex: float('infinity') for vertex in graph}
    # Inicializamos el diccionario de predecesores para reconstruir los caminos
    previous_nodes = {vertex: None for vertex in graph}
    # La distancia desde el nodo inicial a sí mismo es cero
    distances[start] = 0
    # Creamos una cola de prioridad y añadimos el nodo inicial
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Extraemos el nodo con la distancia mínima
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Si encontramos una distancia mayor que la almacenada, continuamos al siguiente
        if current_distance > distances[current_vertex]:
            continue
        
        # Recorremos los vecinos del nodo actual
        for neighbor, weight in graph[current_vertex].items():
            # Calculamos la distancia total desde el nodo inicial hasta el vecino
            distance = current_distance + weight
            
            # Si encontramos un camino más corto al vecino
            if distance < distances[neighbor]:
                # Actualizamos la distancia mínima al vecino
                distances[neighbor] = distance
                # Registramos el nodo actual como predecesor del vecino
                previous_nodes[neighbor] = current_vertex
                # Añadimos el vecino a la cola de prioridad para futuras exploraciones
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Retornamos las distancias mínimas y los predecesores para reconstruir caminos
    return distances, previous_nodes

def reconstruct_path(end_vertex, previous_nodes):
    # Inicializamos una lista para almacenar el camino
    path = []
    # Comenzamos desde el nodo destino
    current_vertex = end_vertex
    while current_vertex is not None:
        # Añadimos el nodo actual al camino
        path.append(current_vertex)
        # Retrocedemos al nodo anterior en el camino
        current_vertex = previous_nodes[current_vertex]
    # Invertimos la lista para obtener el camino desde el inicio hasta el destino
    path.reverse()
    # Retornamos el camino reconstruido
    return path

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},             # Nodo A conectado a B (peso 1) y C (peso 4)
    'B': {'A': 1, 'C': 2, 'D': 5},     # Nodo B conectado a A (1), C (2), D (5)
    'C': {'A': 4, 'B': 2, 'D': 1},     # Nodo C conectado a A (4), B (2), D (1)
    'D': {'B': 5, 'C': 1}              # Nodo D conectado a B (5) y C (1)
}

start_vertex = 'A'  # Definimos el nodo inicial

# Ejecutamos el algoritmo de Dijkstra para obtener distancias y caminos
distances, previous_nodes = dijkstra_with_paths(graph, start_vertex)

# Imprimimos las distancias mínimas desde el nodo inicial a cada nodo
print("Distancias desde el nodo inicial:")
for vertex in distances:
    print(f"Distancia hasta {vertex}: {distances[vertex]}")

# Reconstruimos e imprimimos el camino más corto desde el inicio hasta cada nodo
print("\nCaminos más cortos desde el nodo inicial:")
for end_vertex in graph:
    path = reconstruct_path(end_vertex, previous_nodes)
    print(f"Camino hasta {end_vertex}: {' -> '.join(path)}")
