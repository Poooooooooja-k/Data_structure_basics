class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class singly_linked:
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
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            new_node.ref=n.ref
            n.ref=new_node
    def remove_dup(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==n.ref.data:
                    n=n.ref.ref
LL1=singly_linked()
LL1.add_end(10)
LL1.add_end(20)
LL1.add_end(20)
LL1.remove_dup()
LL1.print_LL()

