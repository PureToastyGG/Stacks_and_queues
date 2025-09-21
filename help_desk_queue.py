# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    
    def peek(self):
        if not self.front:
            return None
        return self.front.value
    
    def print_queue(self):
        current = self.front
        if not current:
            print("The queue is empty.")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    # Create an instance of the Queue class
    help_desk = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            help_desk.enqueue(name)
            # Add the customer to the queue
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            helped_customer = help_desk.dequeue()
            print(f"Helped customer: {helped_customer}") if helped_customer else print("No customers in the queue.")


        elif choice == "3": 
            next_customer = help_desk.peek()
            print(f"Next customer: {next_customer}") if next_customer else print("No customers in the queue.")


        elif choice == "4":
            print("\nWaiting customers:")
            help_desk.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
