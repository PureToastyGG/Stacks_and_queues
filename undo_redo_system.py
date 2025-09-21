# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None
	
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node 

    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
    
    def peek(self):
        if not self.top:
            return None
        return self.top.value
    
    def print_stack(self):
        current = self.top
        if not current:
            print("The stack is empty.")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()
    # Create instances of the Stack class for undo and redo
    

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            # Push the action onto the undo stack and clear the redo stack


            print(f"Action performed: {action}")
        elif choice == "2":
            if not undo_stack.peek():
                print("No actions to undo.")
            else:   
                undid_action = undo_stack.pop()
                redo_stack.push(undid_action)
                print(f"Undid action: {undid_action}")
            # Pop an action from the undo stack and push it onto the redo stack
            

        elif choice == "3":
            if not redo_stack.peek():
                print("No actions to redo.")
            else:
                redid_action = (redo_stack.pop())
                undo_stack.push(redid_action)
                print(f"Redid action: {redid_action}")
            # Pop an action from the redo stack and push it onto the undo stack


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()