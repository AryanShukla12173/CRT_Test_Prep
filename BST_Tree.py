class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
# List of BST Elements
l1 = [100,96,120,99,136]
class BST:
    def __init__(self,data):
        self.root = Node(data[0])
        self.data = data[1:] 
        self.elementInsert()
    # def assignNodes(self, root , newNode):
    #     if root == None:
    #         print("Root is invalid")
    #         return
    #     if newNode.data > root.data:
    #         if root.right == None:
    #             root.right = newNode
    #         else:
    #             self.assignNodes(root.right,newNode)
            
    #     if newNode.data < root.data:
    #         if self.root.left == None:
    #             self.root.left = newNode
    #         else:
    #             self.assignNodes(root.left,newNode)
    
    def assignNodes(self,newNode):
        if self.root == None:
            print("No root node to insert")
        curr = self.root
        while True :
            if newNode.data > curr.data :
                if curr.right == None:
                    curr.right = newNode
                    break
                else: curr = curr.right
            if newNode.data < curr.data:
                if curr.left == None:
                    curr.left = newNode
                    break
                else: curr = curr.left
        
    def elementInsert(self):
        for i in self.data:
            newNode = Node(i)
            self.assignNodes(newNode)
    def BFS(self):
        if self.root == None:
            print("No available nodes")
        queue = []
        queue.append(self.root)
        while queue:
            curr = queue.pop(0)
            print(curr.data,end=" ")
            if curr.left!= None:
                queue.append(curr.left)
            if curr.right!= None:
                queue.append(curr.right)
    
    def preorder_traversal(self):
        if self.root == None:
            print("No available nodes")
        stack = []
        stack.append(self.root)
        curr = 0
        while stack:
            curr = stack.pop()
            print(curr.data,end=" ")
            if curr.right!= None:
                stack.append(curr.right)
            if curr.left!= None:
                stack.append(curr.left)
        
    def postorder(self):
        Stack=[]
        Stack1=[]
        if self.root is None:
            return
        else:
           
            Stack.append(self.root)
            while Stack:
                r=Stack.pop()
                Stack1.append(r)
                if r.left:
                    Stack.append(r.left)
                if r.right:
                    Stack.append(r.right)
            while len(Stack1)!=0:
                print(Stack1.pop().data,end=" ")
    
    def inorder(self):
        if self.root == None:
            print("No node available")
        stack = []
        curr = self.root
        while True:
            if curr!= None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.data,end=" ")
                curr = curr.right
            else:
                break
    
    def PrintEvenandOddValueNodes(self):
        if self.root == None:
            print("No available nodes")
        queue = []
        even = []
        odd = []
        queue.append(self.root)
        while queue:
            curr = queue.pop(0)
            if curr.data % 2 == 0:
                even.append(curr.data)
            if curr.data % 2 != 0:
                odd.append(curr.data)
            if curr.left!= None:
                queue.append(curr.left)
            if curr.right!= None:
                queue.append(curr.right)
        print("Even value Nodes:",even)
        print("Odd value Nodes:",odd)
    
    def MaximumValueInTree(self):
        if self.root == None:
            print("No available nodes")
        queue = []
        queue.append(self.root)
        max1 = 0
        while queue:
            curr = queue.pop(0)
            if max1 < curr.data:
                max1 = curr.data
            if curr.left!= None:
                queue.append(curr.left)
            if curr.right!= None:
                queue.append(curr.right)
        return max1
    
    def MinValueInTree(self):
        if self.root == None:
            print("No available nodes")
        curr = self.root
        while curr.left != None:
            curr = curr.left
        return curr.left.data
l2 = BST(l1)
l2.BFS()
print(' ')
l2.preorder_traversal()
print("")
l2.postorder()
print("")
l2.inorder()
print("")
l2.PrintEvenandOddValueNodes()
print("")
print("Maximum Element in Tree:",l2.MaximumValueInTree())
print("")
print("Mininum Element in Tree:",l2.MinValueInTree())