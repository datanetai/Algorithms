# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees
from BST.BST import Node
# indorder
def isValidBST(root: Node) -> bool:
    if root == None:
        return True
    stack = []
    prev = None
    while root != None or len(stack) > 0:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev != None and root.data <= prev.data:
            return False
        prev = root
        root = root.right
    return True

# recursive
def isValidBST2(root: Node) -> bool:
    if root == None:
        return True
    def helper(root, min, max):
        if root == None:
            return True
        if root.data <= min or root.data >= max:
            return False
        return helper(root.left, min, root.data) and helper(root.right, root.data, max)
    return helper(root, float('-inf'), float('inf'))

tree = Node(2)
tree.left = Node(1)
tree.right = Node(3)
tree.left.left = Node(0)
tree.left.right = Node(4)
#      2
#    /   \
#   1     3
#  / \
# 0   4

print(isValidBST(tree)) # False