class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
        else:
            self.head=self.head.ref
LL1=linked_list()
LL1.add_begin(10)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.delete_begin()
LL1.print_LL()