class stack:
    def __init__(self):
        self.S=[]
        self.top=0
    def push(self,x):
        self.S.append(x)
        self.top+=1
    def pop(self):
        if self.top==0:
            return None
        self.top-=1
        return self.S.pop()
    def empty(self):
        if self.top==0:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        self.Q=[]
        self.front=0
        self.rear=0
    def enqueue(self,x):
        self.Q.append(x)
        self.rear+=1
    def dequeue(self):
        x=self.Q[self.front]
        if self.front==self.rear:
            self.front=0
            self.rear=0
        else:
            self.front+=1
        return x

class QueuePythonic:
    def __init__(self):
        self.Q=[]
    def enqueue(self,x):
        self.Q.append(x)
    def dequeue(self):
        if self.Q==[]:
            return None
        else:
            return self.Q.pop(0)
            
def test_stack():
    S=stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    assert S.pop()==4
    assert S.pop()==3
test_stack()

def test_queue():
    Q=Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    assert Q.dequeue()==1
    assert Q.dequeue()==2
    assert Q.dequeue()==3
    assert Q.dequeue()==4
test_queue()