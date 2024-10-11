class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)


def dfs_with_stack(start_node):
    stack = [start_node]
    visited = set()
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            print(current_node.value)
            
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_C)
node_B.add_neighbor(node_D)
node_C.add_neighbor(node_E)

dfs_with_stack(node_A)
