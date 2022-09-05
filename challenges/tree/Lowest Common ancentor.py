# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
from BST.BST import Node
def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    if root.data > p.data and root.data > q.data:
        return lowestCommonAncestor(root.left, p, q)
    elif root.data < p.data and root.data < q.data:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root

# iterative solution
def lowestCommonAncestor2(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    while root:
        if root.data > p.data and root.data > q.data:
            root = root.left
        elif root.data < p.data and root.data < q.data:
            root = root.right
        else:
            return root
    
tree = Node(6)
tree.left = Node(2)
tree.right = Node(8)
tree.left.left = Node(0)
tree.left.right = Node(4)
tree.left.right.left = Node(3)
tree.left.right.right = Node(5)
tree.right.left = Node(7)
tree.right.right = Node(9)
p = tree.left
q = tree.right
print(lowestCommonAncestor(tree, p, q).data)