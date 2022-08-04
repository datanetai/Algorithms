# create graph using adjacency list
class Graph:
    def __init__(self,directed=True):
        self.graph = {}
        self.directed = directed
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        self.graph[vertex1].append(vertex2)
        if not self.directed:
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for key in sorted(list(self.graph.keys())):
            print(key, '->', self.graph[key])
        




# Hierholzer’s Algorithm eulerian cycle
def eulerian_cycle(graph):
    # find in and out degree of each vertex
    in_degree = {}
    out_degree = {}
    for vertex in graph:
        in_degree[vertex] = 0
        out_degree[vertex] = 0
    for vertex in graph:
        for neighbour in graph[vertex]:
            out_degree[vertex] += 1
            in_degree[neighbour] += 1
    
    print('in_degree:', in_degree)
    print('out_degree:', out_degree)
    #check if every vertex has even degree
    #by theorem 1.20 graph does not contain  eulerian cycle if every vertex does not have even degree or in degree is not equal to out degree
    for vertex in graph:
        if (in_degree[vertex]!=out_degree[vertex]):
            return None
        
    stack = []
    path = []
    start = next(iter(graph))
    stack.append(start)
    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            stack.append(graph[vertex].pop())
        else:
            path.append(stack.pop())
    #check if path contains all edges
    if path and path[0] == path[-1]:
        return path

#test eulerian_cycle
g=Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_edge('a','b')
g.add_edge('b','c')
g.add_edge('c','d')
g.add_edge('d','e')
g.print_graph()

print(eulerian_cycle(g.graph))
