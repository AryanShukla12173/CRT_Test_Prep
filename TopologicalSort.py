"""
Topological Sort is only applicable on directed acyclic graph
Topological Sort using DFS will be done using outdegree
Topological Sort using BFS will be done using indegree
ALGO:
append all vertices with 0 indegree
pop an element
check for the vertex for whom it was  a neighbour and accordingly calculate new dregree for those vertices
repeat
"""

class Graph:
    def __init__(self) -> None:
        self.graph= {}
        self.indegree = []
    def addUndirectedEdges(self,FirstNode,SecondNode,cost):
        if FirstNode not in self.graph:
            self.graph[FirstNode] = []
        if SecondNode not in self.graph:
            self.graph[SecondNode] = []
        self.graph[FirstNode].append((SecondNode,cost))
        self.graph[SecondNode].append((FirstNode,cost))
    def addDirectedEdges(self,fromNode,ToNode,cost):
        if fromNode not in self.graph:
            self.graph[fromNode] = []
        if ToNode not in self.graph:
            self.graph[ToNode] = []
        self.graph[fromNode].append((ToNode,cost))
        
    def BFS(self,startNode):
        vis = set()
        que = []
        que.append(self.graph[startNode])
        vis.add(startNode)
        while que:
            curr = que.pop(0)
            print(curr,end='->')
            for i in self.graph[curr]:
                if i not in vis:
                    que.append(i)
                    vis.add(i)
        print("None")
    def inDegreeCalc(self):
        if len(self.graph) == 0 :
            print("Graph is empty")
            return 
        indegree = {}
        keys = self.graph.keys()
        count = 0
        for i in keys:
            count = 0
            # print(i)
            for key1,value in self.graph.items():
                if i != key1:
                    for key2,_ in value:
                        if key2 == i:
                            count += 1
                            print(f"condition triggered for {i}")
                else:
                    continue
        
            indegree[i] = count
        self.indegree = indegree
        print(indegree)            
        
    def TopologicalSort(self):
        indegree_copy = self.indegree
        queue = []
        topo = []
        pass 
        
            
                
                
                    
    # def AdjacencyMatrix(self): Complete the implementation
    #     inf = float('inf')
    #     count = len(self.graph)
    #     matrix = [[0 for _ in range(count)] for _ in range(count)]
    #     print(matrix)
    #     for  keys1,values1 in self.graph.items():
    #         for keys2,values2 in  self.graph.items():
    #             if keys1 == startNode:
    

    def DisplayGraph(self):
        print(self.graph)
    
g = Graph()
g.addDirectedEdges('a','b',5)
g.addDirectedEdges('a','c',6)
g.addDirectedEdges('b','d',7)
g.addDirectedEdges('c','d' ,10)
g.DisplayGraph()
g.inDegreeCalc()
# g.TopologicalSort()