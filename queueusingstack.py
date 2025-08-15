
class QueueUsingStack:
    def __init__(self) -> None:
        self.primarystack = []
        self.secondarystack= []
        self.front = -1
        self.rear = -1
    def push(self,num):
        self.primarystack.append(num)
        # self.front = self.primarystack[-1]
        # self.rear =  self.secondarystack[-1]
        print(f"{num} is enqueued into queue")
    def pop(self):
        while self.primarystack:
            ele = self.primarystack.pop()
            # print(f"{ele} has been popped from first stack")
            self.secondarystack.append(ele)
        # print(self.secondarystack)
        print("All elements shifted from stack 1 to stack2")
        ele = self.secondarystack.pop()
        print(f"Element {ele} has been dequeued from the queue")
            
    # def peek(self):
    #     if self.primarystack:
    #         self.front = self.primarystack[-1]
    #         self.rear = 0
    #     print(f"rear ele is {self.primarystack[self.rear]} and front is at {self.front}")

Queue1 = QueueUsingStack()
Queue1.push(1)
Queue1.push(2)
Queue1.push(3)
Queue1.pop()
# Queue1.peek()    
    
        