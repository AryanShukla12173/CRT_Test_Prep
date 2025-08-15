#AVL TREE
### Balance Factor : H(L) - H(R) where H is height of left and right subtree acceptable for any node is 0,1,-1
### We can only perform two types of rotation left and right rotations which are applied in cases of an unbalanced tree
## if we have nodes 10->11->12 this will be a complete right subtree which can be corrected using Left rotation of 10 then we get 11 will become parent of 10 and 12 10<-11->12 thus making the tree balanced
# Similarly if we have a BST with only a left subtree    7<-8<-9 we can correct this tree by using a right rotation on 9 which makes 8 a parent of 7 and 9
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
elements = [8,9,10]
class AVL:
    def __init__(self,list):
        self.root = Node(list[0])
        self.data = list[1:]
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    
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
    def tree_construction(self):
        for i in self.data:
            newNode = Node(i)
            self.assign(self.root,newNode)
            print(self.balance_factor(newNode))
            if self.balance_factor(newNode)  not in [1,0,-1]:
                
                print("Tree is unbalanced")
                return 
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
    
a = AVL(elements)
a.tree_construction()
a.traversal()
        
        