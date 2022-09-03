# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.
from BST.BST import Node

def hasPathSum(root: Node, targetSum: int) -> bool:
    if not root:
        return False
    stack = [(root, targetSum - root.data)]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            stack.append((node.left, curr_sum - node.left.data))
        if node.right:
            stack.append((node.right, curr_sum - node.right.data))
    return False

# solution 2 recursive
def hasPathSum(root: Node, targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.data
    return hasPathSum(root.left, targetSum - root.data) or hasPathSum(root.right, targetSum - root.data)

tree = Node(5)
tree.left = Node(4)
tree.right = Node(8)
tree.left.left = Node(11)
tree.left.left.left = Node(7)
tree.left.left.right = Node(2)
tree.right.left = Node(13)
tree.right.right = Node(4)
tree.right.right.right = Node(1)

# draw tree
print(hasPathSum(tree,22)) # True