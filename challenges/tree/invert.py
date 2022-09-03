from BST.BST import Node

# Given the root of a binary tree, invert the tree, and return its root.

def invertTree(root: Node) -> Node:
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
    
# solution 2 iterative
def invertTree(root: Node) -> Node:
    if root is None:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root

tree = Node(4)
tree.left = Node(2)
tree.right = Node(7)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.left = Node(6)
tree.right.right = Node(9)

resulted_tree = invertTree(tree)  # 4 7 2 9 6 3 1
