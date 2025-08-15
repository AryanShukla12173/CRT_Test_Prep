class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.start = None
        self.tail = None
    @staticmethod
    def createNode(data):
        new_node  = Node(data)
        return new_node
    def InsertAtBeginning(self,data):
        new_node = self.createNode(data)
        if self.start == None:
            self.start = new_node
            self.tail = new_node
        else:
            new_node.next = self.start
            self.start = new_node
    def InsertAtEnd(self,data):
        new_node = self.createNode(data)
        if self.start == None:
            self.start = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
    def InsertInMiddle(self,data,key):
        new_node =  Node(data)
        if self.start == None:
            print("List is empty inserting at beginning")
            self.start = new_node
            self.tail = new_node
        else:
            temp = self.start
            while temp.data!=key:
                temp = temp.next
                if temp == None or temp == self.tail:
                    print("Element not present in list")
                    return
            temp1 = temp.next
            temp.next = new_node
            new_node.next = temp1
    def DeleteAtBeginning(self):
        if self.start == None:
            print("List is empty")
        else:
            self.start = self.start.next
    def DeleteAtEnd(self):
        if self.start == None:
            print("List is empty")
        elif self.start == self.tail:  # Only one node
            print(f"Deleted {self.tail.data}")
            self.start = None
            self.tail = None
        else:
            temp = self.start
            while temp.next!=self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp     
    def DeleteSpecificValueNode(self,key):
        if self.start == None:
            print("List is Empty")
        temp = self.start
        if temp.data == key:
            self.start = self.start.next
            return
        while temp.next.data != key:
            temp = temp.next
        temp.next = temp.next.next
    def reverse(self):
        pass
                         
    def DisplayList(self):
        if self.start == None:
            print("List is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end="->")
                temp = temp.next
            print('None')
    
l1 = LinkedList()
l1.DisplayList()
l1.InsertAtBeginning(10)
l1.DisplayList()
l1.InsertAtEnd(20)
l1.DisplayList()
l1.InsertAtBeginning(30)
l1.DisplayList()
l1.InsertAtBeginning(40)
l1.DisplayList()
l1.InsertInMiddle(35,40)
l1.DisplayList()
l1.InsertInMiddle(21,20)
l1.DisplayList()
l1.InsertInMiddle(25,25)
l1.DisplayList()
l1.DeleteAtBeginning()
l1.DisplayList()
l1.DeleteAtEnd()
l1.DisplayList()    
l1.DeleteSpecificValueNode(30)
l1.DisplayList()   
            
            
            
        
        
        