class Vertex:
    def __init__(self,name):
        self.neighbors = {}
        self.visited = False
        self.name=name
        self.distance = 0
        # self.parent = None
        # self.distance = 0
        # self.color = 'white'
        # self.discovery = 0
        # self.finish = 0

    def addNeighbor(self, neighbor,distance):
        self.neighbors[neighbor] = distance
    
    def __str__(self):
        return self.name

class Graph:
    def __init__(self,isDirected=False):
        self.vertList = {}
        self.numVertices = 0
        self.isDirected = isDirected
    #add edge with distance
    def addEdge(self,start,end,distance):
        if start not in self.vertList:
            self.addVertex(start)
        if end not in self.vertList:
            self.addVertex(end)
        self.vertList[start].addNeighbor(self.vertList[end],distance)
        if self.isDirected == False:
            self.vertList[end].addNeighbor(self.vertList[start],distance)
    def addVertex(self,key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
    def returnNeighbors(self,vertex):
        neigbhours = []
        for n in vertex.neighbors:
            neigbhours.append(n.name)
        return neigbhours

    def dijkstra(self,start,end):
        q = []
        prev=[start.name]
        for vert in self.vertList:
            self.vertList[vert].distance = float('inf')
            q.append(self.vertList[vert])
        start.distance = 0

        q.append(start)
        while len(q) > 0:
            #min q
            u = q[0]
            
            q.remove(u)
            for n in u.neighbors:
               
                alt =u.distance + u.neighbors[n]
                if alt < n.distance:
                    n.distance = alt
                    
                    prev.append(n)

        
        #all distances
        printPath(prev,end)
        return end.distance,prev
#print path
def printPath(prev,end):
    path = []
    path.append(end)
    while end in prev:
        end = prev.pop()
        path.append(end)
    path.reverse()
    #loop over path
    for v in path:
        print(v.name)
#test graph
g = Graph()
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')
g.addVertex('E')
g.addEdge('A','B',2)
g.addEdge('A','C',3)
g.addEdge('B','D',1)
g.addEdge('C','E',5)
g.addEdge('D','E',6)
g.addEdge('D','C',1)
# print(g.returnNeighbors(g.vertList['A']))

print(g.dijkstra(g.vertList['A'],g.vertList['E']))