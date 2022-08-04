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
        
#implement dfs
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex])
    return visited

#recursive dfs
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

#topological sort using dfs
def topological_sort(G,node):
    result=[]
    seen=set()
    def helper(node):
        for n in G[node]:
            if n not in seen:
                seen.add(n)
                helper(n)
        result.append(node)
    helper(node)
    return result[::-1]

            
    


    
# test graph
# g = Graph(directed=False)
# g.add_vertex('a')
# g.add_vertex('b')
# g.add_vertex('c')
# g.add_vertex('d')
# g.add_vertex('e')
# g.add_edge('a', 'b')
# g.add_edge('a', 'c')
# g.add_edge('a', 'd')
# g.add_edge('b', 'e')
# g.add_edge('c', 'd')
# g.add_edge('c', 'e')
# g.add_edge('d', 'e')
# g.print_graph()

# #test dfs
# print(dfs(g.graph, 'a'))
def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)              # this line replaces the result.append line

    recursive_helper(node)
    return result
G=Graph(directed=False)
G.add_edge( "dpkg", "multiarch_support" )
G.add_edge( "dpkg", "coreutils" )
G.add_edge( "dpkg", "tar" )
G.add_edge( "dpkg", "libbz2" )
G.add_edge( "coreutils", "libbz2" )
G.add_edge( "coreutils", "libselinux1" )
G.add_edge( "libbz2", "libselinux1" )
G.add_edge( "libselinux1", "multiarch_support" )

S=topological_sort(G.graph,'multiarch_support')
T=recursive_topological_sort(G.graph,'dpkg')
print(S)