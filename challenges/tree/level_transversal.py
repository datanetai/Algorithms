# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from BST.BST import Node

def levelOrder(root: Node) -> list[list[int]]:
    if not root:
        return []
    queue = [root] 
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


def maxDepth(root: Node) -> int:
    if not root:
        return 0
    level = 0
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level

# same solution as above, but using little different approach 
def minDepth2(root: Node) -> int:
    if not root:
        return 0
    level = 0
    queue = [root]
    num_nodes = 1
    while queue:
        node = queue.pop(0)
        num_nodes -= 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if num_nodes == 0:
            level += 1
            num_nodes = len(queue)
    return level

#  Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
 
def isSymmetric(root: Node) -> bool:
    if not root:
        return True
    return isSymmetricHelper(root.left, root.right)
def isSymmetricHelper(left: Node, right: Node) -> bool:
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.data != right.data:
        return False
    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
    
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
print("levelOrder: ", levelOrder(tree))
print("maxDepth: ", maxDepth(tree))
print("isSymmetric: ", isSymmetric(tree))