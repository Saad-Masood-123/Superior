# BFS without Queue & without Node

def bfs(graph, start):
    visited = []
    level = [start]
    
    while level:
        next_level = []
        for node in level:
            if node not in visited:
                visited.append(node)
                next_level.extend(graph[node])
        level = next_level
    
    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print("BFS Traversal: ", bfs(graph, 'A'))
