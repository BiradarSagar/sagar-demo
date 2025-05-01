from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Since the graph is undirected, add edges both ways
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
g = Graph()

# Adding edges to the undirected graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("Depth First Search (DFS) starting from vertex 0:")
g.dfs_recursive(0)

print("\nBreadth First Search (BFS) starting from vertex 0:")
g.bfs(0)

#DFS Time=O(v) Space=O(v)
#BFS Time=O(V+ E) Space=O(v)
