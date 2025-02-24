import heapq

def dijkstra(graph, start):
    # Inicialización de distancias y cola de prioridad
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Si se encuentra una distancia mayor, se ignora
        if current_distance > distances[current_vertex]:
            continue
        
        # Revisión de vecinos y actualización de distancias
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Solo se consideran caminos más cortos
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
print(dijkstra(graph, start_vertex))
