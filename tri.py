"""
Trie is a concept wherein we create graphs of words such as apple,app,ape etc this allows for various applications such as autocomplete
To Do: Add a universal root for the graph
       add a way to search any string that exists with the graph
       Count words with prefix 
       Autocomplete for  a word
       Longest Prefix Match
       
"""
class GraphNode:
    def __init__(self,char,Flag) -> None:
        self.char = char
        self.endofWord = Flag

class Graph:
    def __init__(self,word):
        self.g = {}
        graph_nodes_list = []
        i = 0
        j = i+1
        for index,ele in enumerate(word):
            if index == len(word)-1:
                newNode = GraphNode(ele,True)
                graph_nodes_list.append(newNode)
            else:
                newNode = GraphNode(ele,False)
                graph_nodes_list.append(newNode)

        while j != len(graph_nodes_list):
            g.addEdgesDirected(fromNode=graph_nodes_list[i],toNode=graph_nodes_list[j])
            i +=1
            j+=1 
        
        
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
    def searchWord(self):
        pass
    def deleteWord(self,word):
        end_char =  word[-1]
        for i in self.g.keys():
            if end_char == i.char:
                i.endofWord = False
        print("Word is deleted")
        
             
    def displayGraph(self):
        for key,value in self.g.items():
            print(f"{key.char} and {key.endofWord} : {value}")
    
    def AdjacencyMatrix(self):
        pass
    def displayWord(self):
        pass
    

# Create graph nodes for a specific word
word = input()
g = Graph(word)
g.displayGraph()
g.deleteWord(word)
g.displayGraph()