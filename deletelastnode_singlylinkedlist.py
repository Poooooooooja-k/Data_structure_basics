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
    def add_before(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        elif self.head.ref is None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
                n.ref=None
LL1=linked_list()
LL1.add_before(20)
LL1.add_before(30)
LL1.delete_end()
LL1.print_LL()