import heapq

def prim_mst(graph, start_node):
    visited = set()
    min_heap = [(0, start_node)]  # (weight, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if u in visited:
            continue
        
        visited.add(u)
        total_cost += weight

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))
        
        if weight != 0:  # To skip adding start node edge (0 weight)
            mst_edges.append((u, weight))

    return mst_edges, total_cost

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
    graph[v].append((u, weight))  # Because graph is undirected

start_node = input("Enter the starting node: ")

mst_edges, total_cost = prim_mst(graph, start_node)

print("\nEdges in MST:")
for node, weight in mst_edges:
    print(f"{node} with weight {weight}")

print(f"Total cost of MST: {total_cost}")
