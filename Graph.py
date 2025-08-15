""" A tree is a connected graph which has no edges which will form a cycle that is  a tree is acyclic in nature
A complete graph is a graph with nodes that are all connected to each other
a coNNECTed GRAPh is a gRAPH Where aLL nodeS ARE ReacHABLE

MULTIGRAPH
WEIghted graPH
CYCLIC grapH
ways TO REPresENT grAPHs ARE adjacENCy maTRIx and ADJacencY LISt

"""
class Graph:
    def __init__(self):
        self.g = {}
        
    def addedges(self,u,v):
        if u not in self.g:
            self.g[u] = []
        if v not in self.g:
            self.g[v] = []
        self.g[u].append(v)
        self.g[v].append(u)
    def addEdgesDirected(self,fromNode,toNode):
        if fromNode not in self.g:
            self.g[fromNode] = []
        if toNode not in self.g:
            self.g[toNode] = []
        self.g[fromNode].append(toNode)
        
    def BFS(self,startNode):
        visited = set()
        queue = []
        queue.append(startNode)
        visited.add(startNode)
        while queue:
            curr = queue.pop(0)
            print(curr,end="->")
            for i in self.g[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        print("None")
        
    def DFS(self,startNode):
        vis = set()
        stack = []
        stack.append(startNode)
        while stack:
            curr = stack.pop()
            print(curr,end="->")
            for  i in self.g[curr]:
                if i not in vis:
                    vis.add(i)
                    stack.append(i)
        print('None')    
        
    def displayGraph(self):
        print(self.g)
    
    def AdjacencyMatrix(self):
        pass
x = Graph()
x.addedges('a','b')
x.addedges('a','d')
x.addedges('b','c')
x.addedges('c','d')
x.addedges('d','b')
# x.addEdgesDirected('a','b')
# x.addEdgesDirected('c','d')
# x.addEdgesDirected('e','f')
# x.addEdgesDirected('e','a')
# x.displayGraph()
x.BFS('a')
x.DFS('a')
