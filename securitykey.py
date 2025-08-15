# total_payload_size = 64
# payload = 0
# payload = input()
# count = 1
# dist = []
# for i  in payload:
#     if i not in dist:
#         dist.append(i)
#     else:
#         count+= 1
# print(f"The Security Key is: {count}")

class Node:
 def __init__(self,data):
  self.data = data
  self.next = None
#  @staticmethod
#  def display(s):
#   if s == None:
#    print("List is empty")
#   else:
#     while s!= None:
#         print(s.data)
#         s = s.next

# node1 = Node(10);
# node1.next = Node(20);
# node1.next.next = Node(30);
# node1.next.next.next= Node(40)
# Node.display(node1)
class LinkedList:
  def __init__(self):
    self.start = None
  
  def insertAtStart(self):
    data = int(input("Enter the node value:"))
    node = Node(data)
    if self.start == None:
      self.start = node
      return
    node.next = self.start
    self.start = node
  
  def insertAtEnd(self):
    data = int(input("Enter the value:"))
    node = Node(data)
    if self.start == None:
      self.start = node
      return 
    temp = self.start
    while temp.next != None:
      temp = temp.next
    temp.next = node
   
  def insert_in_between(self):
    val = int(input("Enter the value to be searched after which node will be inserted:"))
    data = int(input("Enter the value of the node:"))
    node  = Node(data)
    if self.start == None:
      temp = self.start
    while temp.data != val:
      temp = temp.next
    node.next = temp.next
    temp.next = node
  def display(self):
    temp = self.start
    if temp ==  None:
     print("List is empty")
     return
    while temp != None:
      print(temp.data)
      temp = temp.next


list = LinkedList()
list.insertAtEnd()
list.insertAtEnd()
list.insert_in_between()
list.display()
