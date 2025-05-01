import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y)
        self.parent = parent

        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost from this node to goal
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reversed path

        x, y = current_node.position
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for nx, ny in neighbors:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                neighbor_pos = (nx, ny)
                if neighbor_pos in closed_set:
                    continue

                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_pos, end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                # Check if neighbor is already in open_list with a lower f
                if any(n.position == neighbor_node.position and n.f <= neighbor_node.f for n in open_list):
                    continue

                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example Grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = astar_search(grid, start, end)

print("Path found:" if path else "No path found.")
print(path)
#Time Complexity:O(E * log(v))
#Space Complexity:O(v)
