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
    # Sort edges based on weight
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
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []
print("Enter edges (format: u v weight) one per line:")
for _ in range(edges_count):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

mst, total_cost = kruskal_mst(vertices, edges)

print("\nMinimum Spanning Tree edges (u -- v == weight):")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

print(f"Total cost of MST: {total_cost}")

#Time = O(Elog(v)) Space=O(V+E) 
