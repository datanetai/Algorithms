# Given the root of a binary tree, return the inorder traversal of its nodes' values.
from BST.BST import Node
# recursive solution
# Time complexity O(n)
# Space complexity O(n)
def inorderTraversal(root: Node) -> list[int]:
    if root == None:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)

# iterative solution
# Time complexity O(n)
# Space complexity O(n)
def inorderTraversal2(root: Node) -> list[int]:
    if root == None:
        return []
    res = []
    stack = []
    while True:
        if root != None:
            stack.append(root)
            root = root.left
        elif stack != []:
            root = stack.pop()
            res.append(root.data)
            root = root.right
        else:
            break
    return res
        
# Time complexity O(n)
# Space complexity O(1)
def inorderTraversal3(root: Node) -> list[int]:
    if root == None:
        return []
    res = []
    cur = root
    while cur != None:
        if cur.left == None:
            res.append(cur.data)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right != None and pre.right != cur:
                pre = pre.right
            if pre.right == None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                res.append(cur.data)
                cur = cur.right
    return res

# recursive solution
def preorderTraversal(root: Node) -> list[int]:
    if root == None:
        return []
    return [root.data] + preorderTraversal(root.left) + preorderTraversal(root.right)

# iterative solution
def preorderTraversal2(root: Node) -> list[int]:
    if root == None:
        return []
    res = []
    stack = []
    stack.append(root)
    while stack != []:
        root = stack.pop()
        res.append(root.data)
        if root.right != None:
            stack.append(root.right)

        if root.left != None:
            stack.append(root.left)
            
    return res

def postorderTraversal(root: Node) ->list[int]:
    if root == None:
        return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.data]

def postorderTraversal2(root: Node) ->list[int]:
    if root == None:
        return []
    res = []
    stack = []
    stack.append(root)
    while stack != []:
        root = stack.pop()
        res.append(root.data)
        if root.left != None:
            stack.append(root.left)
        if root.right != None:
            stack.append(root.right)
    return res[::-1]
# test
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
res = inorderTraversal2(root)
print(res) # [4, 2, 5, 1, 6, 3, 7]
res = preorderTraversal2(root) # [1, 2, 4, 5, 3, 6, 7]
print(res)
res = postorderTraversal2(root) # [4, 5, 2, 6, 7, 3, 1]
print(res)