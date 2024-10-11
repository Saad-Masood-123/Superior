class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

print("Preorder Traversal: ")
preorder_traversal(root)

print("\nInorder Traversal: ")
inorder_traversal(root)

print("\nPostorder Traversal: ")
postorder_traversal(root)
