# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
from BST.BST import Node
def searchBST(root: Node, val: int) -> Node:
    if not root:
        return None
    if root.data == val:
        return root
    elif root.data > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

# complexity: O(log n) time and O(1) space
# iterative
def searchBST2(root: Node, val: int) -> Node:
    while root:
        if root.data == val:
            return root
        elif root.data > val:
            root = root.left
        else:
            root = root.right
    return None

# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

def insertIntoBST(root: Node, val: int) -> Node:
    if root == None:
        root = Node(val)
        return root
    tmp = root
    while tmp != None:
        if tmp.data > val:
            if tmp.left == None:
                tmp.left = Node(val)
                tmp.left.parent = tmp
                break
            else:
                tmp = tmp.left
        else:
            if tmp.right == None:
                tmp.right = Node(val)
                tmp.right.parent = tmp
                break
            else:
                tmp = tmp.right
    return root

# complexity: O(log n) time and O(1) space
# recursive
def insertIntoBST2(root: Node, val: int) -> Node:
    if root == None:
        root = Node(val)
        return root
    if root.data > val:
        root.left = insertIntoBST2(root.left, val)
    else:
        root.right = insertIntoBST2(root.right, val)
    return root
    




tree = Node(4)
tree.left = Node(2)
tree.right = Node(7)
tree.left.left = Node(1)
tree.left.right = Node(3)
print(searchBST(tree, 2)) # 2
print(insertIntoBST(tree, 5)) # 4 2 1 3 5 7
