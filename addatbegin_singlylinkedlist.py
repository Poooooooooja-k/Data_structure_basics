class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
       
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.ref:
            last_node = last_node.ref
        last_node.ref = new_node
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# Create an instance of LinkedList
LL1 = LinkedList()

# User inserts a set of elements into the list
while True:
    input_data = input("Enter data for the list (enter 'exit' to stop): ")
    if input_data.lower() == "exit":
        break
    try:
        data = int(input_data)
        LL1.append(data)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# User inserts an additional element at the beginning
try:
    additional_data = int(input("Enter an element to insert at the beginning: "))
    LL1.add_begin(additional_data)
except ValueError:
    print("Invalid input. Please enter an integer.")

# Print the final linked list
LL1.print_LL()
