# # A General tree is a tree with n no. of children we need to maintain a dictionary for a list of all children for a given node
# # Degree of  a Node is the total no. of its children 
# # Terminal or Leaf Node are the nodes with no children
# # Ancestor Nodes: No. of parent nodes throughtout the entire tree 
# # Descedent Nodes: No. of nodes which are children and subchildren in the tree
# # Uncle Nodes
# # Binary Tree : A Tree where each node has atmost two children
# # Level
# # Height : Longest edge in the tree
# # Complete Binary Tree: All children must be at the same level
# # Strict Binary Tree : All levels of tree must have exact two children or 0 children
# # Extended Binary Tree : Converting a binary tree with some modification is known as a extended Binary Tree
# # Diameter  of Tree: Longest path between two nodes in a tree
# # Width of Tree: Maximum level of leaf nodes in a level of the tree
# # Traversing Strategies for Tree:
# # (DFS Traversal) : Has subtypes such as inorder , postorder and preorder
# # Level Order Traversal (BFS Traversal)
# # inorder traversal : left root right
# # preorder traversal : root left right
# # postorder traversal : left right root
# # from collections import deque
# # import sys
# # class Node:
# #     def __init__(self, data) -> None:
# #         self.left : Node | None = None
# #         self.right : Node | None  = None
# #         self.data = data

# # root = Node(1)
# # root.left = Node(2) 
# # root.right = Node(3)
# # root.left.left = Node(4)
# # root.left.right = Node(5)
# # root.right.left = Node(6)
# # root.right.right = Node(7)
# # class BFS:
# #     def __init__(self,root) -> None:
# #         self.root = root
# #         self.queue1 = deque()
# #         self.visited = list()
# #     def traversal(self):
# #         node : Node = self.root
# #         while True:
# #             if root is None:
# #                 print("No nodes available")
# #                 break
# #             # Enqueue Operation
# #             self.queue1.append(node)
# #             # Dequeue Operation
# #             node = self.queue1.popleft()
# #             print(f"Element visited : {node.data}")
# #             self.visited.append(node)
# #             # Check if left and right exists
# #             if node.left != None and node.left not in self.visited:
# #                 node= node.left
# #                 self.queue1.append(node)
# #             elif node.right != None and node.right not in self.visited:
# #                 node.right
# #                 self.queue1.append(node)
# #             else:
# #                 print("node not available")
# #                 break
# #t1 = BFS(root=root)    check this implementation

# # BST Tree
from collections import deque
elements = [100,50,120,89,67,43,20,78,125,130,132,123,109]
class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right  = None
        self.data = data 


class BST:
    def __init__(self,data) -> None:
        self.root : Node  = Node(data[0])
        self.data = data[1:]
        self.insertion()
    def assign(self, root, newNode):
        if newNode.data < root.data:
            if root.left is None:
                root.left = newNode
            else:
                self.assign(root.left, newNode)
        else:
            if root.right is None:
                root.right = newNode
            else:
                self.assign(root.right, newNode)

    def insertion(self):
        for i in self.data:
            newNode = Node(i)
            self.assign(self.root, newNode)
    def LOT(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            curr = queue.popleft()
            print(curr.data, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def traversal(self):
        self.LOT()
    def searchElement(self, data):
        if self.root is None:
            print("No Nodes available")
            return
        queue1 = deque()
        queue1.append(self.root)
        curr  = None
        while queue1:
            curr = queue1.popleft()
            if curr.left:
                queue1.append(curr.left)
            if curr.right:
                queue1.append(curr.right)
            if curr.data == data:
                print(f"{data} with node is found")
                return curr
    # def deleteNode(self,data):
    #     current_node = self.searchElement(data)
    #     if current_node.left == None and current_node.right == None:
    #         del current_node
    #     if current_node.right != None and current_node.left == None or current_node.right == None and current_node.left != None:
    #         del current_node
    #     if current_node.right != None and current_node.left != None:
    #         pass
    #     return
    
    def inorder_traversal(self):
        curr = self.root
        stack = []
        while True:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.data, end=" ")
                curr = curr.right
            else:
                break
    # def inorder_traversal(self,root):
    #     if self.root == None:
    #         return
    #     self.inorder_traversal(self.root.left)
    #     print(self.root.data)
    #     self.inorder_traversal(self.root.right)
    
    def delete(self,root,key):
         if root is None:
             return root
         if key < root.data :
             root.left = self.delete(root.left,key)
         elif key > root.data:
             root.right  = self.delete(root.right,key)
         else:
             if root.left is None or root.right is None:
                 return None
             if root.left is None:
                 return root.right
             elif root.right is None:
                 return root.left
             temp  = self.inorder_successor(root.right)
             root.data = temp.data
             root.right = self.delete(root.right,temp.data)
    # def inorder_successor(self):
    #     pass
    # def postorder_traversal(self):
    #     if self.root == None:
    #         print("Nodes are not available")
    #     stack1 = []
    #     stack2  = []
    #     stack1.append(self.root)
    #     while stack1:
            
    def preorder_traversal(self):
        if self.root == None:
            print("No nodes available")
        else:
            stack = []
            stack.append(self.root)
            while stack:
                # stack.append(self.root)
                ele = stack.pop()
                print(ele.data,end=" ")
                if ele.right:
                    stack.append(ele.right)
                if ele.left:
                    stack.append(ele.left)
    
        
        
 

b = BST(elements)
b.preorder_traversal()
print("")
b.inorder_traversal()
# # Preorder Traversal
# # Insertion order should be right child then left child
# # Binary Search Tree Mini and Max Element Search , Even and Odd Value Nodes, Mid Element Display after traversing the whole tree , Calculate the second largest value in the tree
        
        