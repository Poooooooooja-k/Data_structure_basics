class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def remove_dup(self):
        current=self.head
        while current:
            data=current.data
            n=current
            while n and n.ref:
                if n.ref.data==data:
                    n.ref=n.ref.ref
                else:
                    n=n.ref
            current=current.ref
l=linked_list()
l.add_end(10)
l.add_end(20)
l.add_end(20)
l.add_end(30)
l.add_end(40)
l.add_end(10)
l.remove_dup()
l.print_LL()