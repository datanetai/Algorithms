
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,x):
        if self.root == None:
            self.root = Node(x)
        else:
            self.insert_rec(self.root,x)
    def insert_rec(self,root,x):
        """
        recursively insert x into the BST rooted at root.
        """
        if root == None:
            return Node(x)
        elif root.data > x:
            root.left = self.insert_rec(root.left,x)
            root.left.parent = root
        else:
            root.right = self.insert_rec(root.right,x)
            root.right.parent = root
        return root
    
    def insert_iterative(self,x):
        """
        Insert x into the BST rooted at root.
        There are 2 cases:
        1. x is smaller than root.left, insert x to the left of root.left.
        2. x is greater than root.right, insert x to the right of root.right.
        
        """
        root = self.root
        if root == None:
            self.root = Node(x)
            return
        while root != None:
            if root.data > x:
                if root.left == None:
                    root.left = Node(x)
                    root.left.parent = root
                    break
                else:
                    root = root.left
            else:
                if root.right == None:
                    root.right = Node(x)
                    root.right.parent = root
                    break
                else:
                    root = root.right

    def search(self,root,x):
        if root == None:
            return False
        if root.data == x:
            return root
        if root.data > x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)

    def search_iterative(self,x):
        root=self.root
        while root != None:
            if root.data == x:
                return root
            elif root.data > x:
                root = root.left
            else:
                root = root.right
    def minimum(self,root):
        if root == None:
            return None
        else:
            while root.left != None:
                root = root.left
            return root
    def successor(self,x):
        """
        Return the successor of x in the BST.
        Successor is the node with the smallest key greater than x.
        """
        if x.right!=None:
            return self.minimum(x.right)
        else:
            y = x.parent
            while y!=None and x==y.right:
                x = y
                y = y.parent
            return y
    
    def transplant(self,u,v):
        """
        Replace subtree rooted at u with subtree rooted at v."""
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent
  
        
    def delete(self,x):
        """
        Delete the node containing x from the BST."""
        if x.left == None:
            self.transplant(x,x.right)
        elif x.right == None:
            self.transplant(x,x.left)
        else:
            y = self.minimum(x.right)
            if y.parent != x:
                self.transplant(y,y.right)
                y.right = x.right
                y.right.parent = y
            self.transplant(x,y)
            y.left = x.left
            y.left.parent = y
    
    def deletev2(self,x):
        x=self.search_iterative(x)
        print("found {}".format(x.data))
        if x.left == None and x.right == None:
            if x.parent.left == x:
                x.parent.left = None
            else:
                x.parent.right = None

        if x.left==None:
            y=x.right
            y.parent=x.parent
            y.parent.left=y
        elif x.right==None:
            y=x.left
            y.parent=x.parent
            y.parent.right=y
        else:
            z=self.successor(x)
            z_bar=z.parent
            if z_bar.left==z:
                z_bar.left=None
            else:
                z_bar.right=None
            z.parent=x.parent
            z.left=x.left
            z.right=x.right
            if x.parent.left==x:
                x.parent.left=z
            else:
                x.parent.right=z
            


        

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    def preorder(self,root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def inorder_iterative(self,root):
        stack = []
        while True:
            if root != None:
                stack.append(root)
                root = root.left
            elif len(stack) > 0:
                root = stack.pop()
                print(root.data)
                root = root.right
            else:
                break
    
       
        

def inorder(x):

    if x is None:
        return
    inorder(x.left)
    print(x.data, end=' ')
    inorder(x.right)

bst = BST()
def addTo_BST(list):
    
    for i in list:
        bst.insert(i)
    return bst
l=[43,23,545,3,431,54,65,76,87,2]
addTo_BST(l)
bst.delete(bst.search_iterative(43))
bst.inorder_iterative(bst.root)


