class Node:
    """A class to represent a Node in a Singly Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    """A class to represent a Singly Linked List."""
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Link the last node to the new node

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head  # New node points to the current head
        self.head = new_node  # Update head to new node

    def insert_at_position(self, data, pos):
        """Insert a node at a specific position (0-based index)."""
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        count = 0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if not temp:  # Position out of bounds
            print("Position out of range.")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Delete the first node with the given value."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next  # Move head to the next node
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print("Key not found in the list.")
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        """Search for a node with a specific value."""
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return f"Element {key} found at position {pos}."
            temp = temp.next
            pos += 1
        return "Element not found."

    def display(self):
        """Print the linked list elements."""
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Menu-driven program
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Insert at end")
        print("2. Insert at beginning")
        print("3. Insert at position")
        print("4. Delete node")
        print("5. Search for an element")
        print("6. Display list")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter value to insert at end: "))
            sll.insert_at_end(data)
        elif choice == 2:
            data = int(input("Enter value to insert at beginning: "))
            sll.insert_at_beginning(data)
        elif choice == 3:
            data = int(input("Enter value to insert: "))
            pos = int(input("Enter position (0-based index): "))
            sll.insert_at_position(data, pos)
        elif choice == 4:
            key = int(input("Enter value to delete: "))
            sll.delete_node(key)
        elif choice == 5:
            key = int(input("Enter value to search: "))
            print(sll.search(key))
        elif choice == 6:
            sll.display()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
