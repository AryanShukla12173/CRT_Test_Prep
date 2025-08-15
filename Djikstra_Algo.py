"""
Implement Djikstra Algo and Adjacency Matrix
"""
class Graph:
    def __init__(self) -> None:
        self.graph= {}
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
    
    # def AdjacencyMatrix(self): Complete the implementation
    #     inf = float('inf')
    #     count = len(self.graph)
    #     matrix = [[0 for _ in range(count)] for _ in range(count)]
    #     print(matrix)
    #     for  keys1,values1 in self.graph.items():
    #         for keys2,values2 in  self.graph.items():
    #             if keys1 == startNode:
    
    def Djisktra(self,startNode,endNode):
        pass
    def DisplayGraph(self):
        print(self.graph)
    
g = Graph()
g.addUndirectedEdges('a','b',5)
g.addUndirectedEdges('a','c',6)
g.addUndirectedEdges('b','d',7)
g.addUndirectedEdges('c','d' ,10)
# g.BFS('a')
# g.DisplayGraph()
# g.Djikstra_Algo('a')
                