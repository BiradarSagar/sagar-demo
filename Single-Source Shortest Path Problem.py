import heapq

def dijkstra(graph, source):
    # Distance to all nodes set to infinity initially
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we found a better path before, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found
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
    graph[v].append((u, weight))  # If graph is undirected

source = input("Enter source vertex: ")

distances = dijkstra(graph, source)

print("\nShortest distances from source:")
for node in distances:
    print(f"Distance to {node}: {distances[node]}")


#Time:(O(V^2)) Space:(O(V))
