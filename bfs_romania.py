
#BFS searching on Romania map
from collections import deque

graph = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Sibiu": ["Arad", "Fagaras", "Oradea", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Oradea": ["Zerind", "Sibiu"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Rimnicu Vilcea": ["Sibiu", "Pitesti", "Craiova"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Pitesti": ["Rimnicu Vilcea", "Bucharest", "Craiova"],
    "Craiova": ["Rimnicu Vilcea", "Pitesti", "Drobeta"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None

path = bfs(graph, "Arad", "Bucharest")
if path:
    print("Path:", " -> ".join(path))
    print("Number of roads:", len(path) - 1)
else:
    print("No path found.")

