import heapq

def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    visitados = set()
    cola_prioridad = [(0, origen)] 

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

origen = 'A'
resultado = dijkstra(grafo, origen)

for nodo, distancia in resultado.items():
    print(f"Distancia mínima desde {origen} hasta {nodo}: {distancia}")

#O((V + E) log V) V=nodos E=aristas