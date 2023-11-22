class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.nref=None
        self.pref=None
class double_ll:
    def __init__(self) -> None:
        self.head=None
    def print_double(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref
    def add_empty(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            print("list is not empty")
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n 
DDL=double_ll()
DDL.add_begin(20)
DDL.add_begin(30)
DDL.add_end(40)
DDL.add_end(70)
DDL.print_double()


    