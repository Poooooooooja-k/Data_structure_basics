class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self):
        self.head=None
    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.ref:
            last_node = last_node.ref
        last_node.ref = new_node
    def print_LL(self):
        if self.head==None:
            print("the linked list is empty!!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
# ll1=linked_list()
# ll1.append(1)
# ll1.append(2)
# ll1.append(3)
# ll1.print_LL()

# if taking input list from user


# Create an instance of the linked_list
ll1 = linked_list()

# User input loop
while True:
    data_input = input("Enter data for the linked list (type 'exit' to stop): ")
    
    if data_input.lower() == 'exit':
        break
    
    try:
        data = int(data_input)
        ll1.append(data)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Print the linked list
ll1.print_LL()