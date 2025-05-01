class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[xroot] = yroot

def kruskal_mst(vertices, edges):
    # Sort edges by ascending weight
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# Taking input from user
node_mapping = {}
reverse_mapping = {}
counter = 0

vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
print("Enter edges (format: u v weight):")
for _ in range(edges_count):
    u, v, weight = input().split()
    weight = int(weight)

    # Map node names to integers
    if u not in node_mapping:
        node_mapping[u] = counter
        reverse_mapping[counter] = u
        counter += 1
    if v not in node_mapping:
        node_mapping[v] = counter
        reverse_mapping[counter] = v
        counter += 1

    edges.append((node_mapping[u], node_mapping[v], weight))

mst, total_cost = kruskal_mst(vertices, edges)

print("\nEdges in MST:")
for u, v, weight in mst:
    print(f"{reverse_mapping[u]} -- {reverse_mapping[v]} == {weight}")

print(f"Total cost of MST: {total_cost}")

#Time = O(E log E) Space = O(V)
