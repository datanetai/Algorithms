#implement doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
    def append_before_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur =self.head
        prev=None
        while cur.next!=None:
            prev=cur
            cur=cur.next
        temp=prev.next
        prev.next=new_node
        new_node.prev=prev
        new_node.next=temp
    
    def return_list(self):
        cur = self.head
        lst=[]
        while cur:
            lst.append(cur.data)
            cur = cur.next
        print(lst)
        return lst
    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False
    def pop(self):
        if self.head is None:
            print("List is empty")
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        if(cur.prev==None):
            self.head=None
        else: 
            cur.prev.next = None
        return cur.data
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        cur = self.head
        self.head = cur.next
        return cur.data
    def delete(self, data):
        node=self.search(data)
        if node==False:
            print("Node not found")
            return
        if node.prev==None:
            self.head=node.next
            return
        else:
            node.prev.next=node.next

        if node.next!=None:
            node.next.prev=node.prev

class Stack:
    def __init__(self):
        self.ll = LinkedList()
    def push(self, data):
        self.ll.append(data)
    def pop(self):
        return self.ll.pop()
    def return_list(self):
        return self.ll.return_list()

class Queue:
    def __init__(self):
        self.ll = LinkedList()
    def enqueue(self, data):
        self.ll.append(data)
    def dequeue(self):
        return self.ll.delete_first()
    def return_list(self):
        return self.ll.return_list()
#test LinkedList
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append_before_last("C")
assert llist.return_list() == ["A", "C", "B"]
#test stack
stack = Stack()
stack.push("A")
stack.push("B")
assert stack.pop() == "B"
assert stack.pop() == "A"
#test queue
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
assert queue.dequeue() == "A"
assert queue.dequeue() == "B"

            
        

