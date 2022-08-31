class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


# 전위순회
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


# 중위순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)


# 후위순회
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


preorder(root)
print()
inorder(root)
print()
postorder(root)
