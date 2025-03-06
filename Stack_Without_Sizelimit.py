class Stack:
    def __init__(self):
        self.mylist = []
        print("Stack initialized successfully.")

    def push(self, element):
        self.mylist.append(element)
        print("Push operation performed successfully.")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot perform pop operation.")
            return None
        return self.mylist.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        return self.mylist[-1]

    def show(self):
        print("Current Stack:", self.mylist)

    def isEmpty(self):
        return len(self.mylist) == 0  # Direct return

    def delete_stack(self):
        self.mylist.clear()
        print("Stack deleted successfully.")

# Menu-based execution
ch = int(input('1) Create the stack: '))
if ch == 1:
    stack1 = Stack()
    while True:
        choice = int(input('1. Push 2. Pop 3. Peek 4. Delete 5. Check if stack is empty 6. Show stack 7. Delete Stack 8. Exit: '))
        
        if choice == 1:
            el = int(input("Enter the value to be pushed: "))
            stack1.push(el)
        
        elif choice == 2:
            el = stack1.pop()
            if el is not None:
                print("Popped:", el)
        
        elif choice == 3:
            el = stack1.peek()
            if el is not None:
                print("Top element:", el)
        
        elif choice == 4:
            stack1.delete_stack()
        
        elif choice == 5:
            if stack1.isEmpty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        
        elif choice == 6:
            stack1.show()
        
        elif choice == 7:
            del stack1
            print("Stack deleted successfully.")
            break  # Exit loop after deletion
        
        elif choice == 8:
            break
        
        else:
            print("Invalid choice. Please try again.")
