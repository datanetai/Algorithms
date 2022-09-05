# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
from BST.BST import Node
def findTarget(root: Node, k: int) -> bool:
    buffer = {}
    def findTargetHelper(root: Node, k: int) -> bool:
        if root == None:
            return False
        if root.data in buffer:
            return True
        else:
            buffer[k-root.data] = root.data
            return findTargetHelper(root.left,k) or findTargetHelper(root.right,k)
    return findTargetHelper(root,k)


# iterative
def findTarget2(root: Node, k: int) -> bool:
    buffer = {}
    stack = [root]
    while stack:
        node = stack.pop()
        if node.data in buffer:
            return True
        else:
            buffer[k-node.data] = node.data
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False

tree = Node(5)
tree.left = Node(3)
tree.right = Node(6)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.right = Node(7)

target = 9
print(findTarget(tree,target))