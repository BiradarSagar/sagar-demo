import heapq

def dijkstra(graph, source):
    # Initialize distances as infinite
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Min-Heap to store (distance, node)
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we already found a shorter way, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Taking input from user
graph = {}
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

print("Enter edges (format: u v weight):")
for _ in range(edges):
    u, v, weight = input().split()
    weight = int(weight)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, weight))
    graph[v].append((u, weight))  # Comment this line if the graph is directed

source = input("Enter source vertex: ")

distances = dijkstra(graph, source)
#Time = O(E * log(v))  Space=O(v)

print("\nShortest distances from source:")
for node in distances:
    print(f"Distance to {node}: {distances[node]}")
