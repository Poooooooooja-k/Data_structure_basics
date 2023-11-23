class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.nref=None
        self.pref=None
class double_LL:
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
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def delete_begin(self):
        if self.head is None:
            print("linked list is empty")
        if self.head.nref is None:
            self.head =None
        else:
            self.head=self.head.nref
            self.head.pref=None
    def delete_end(self):
        if self.head is None:
            print("linked list is empty")
        if self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def delete_by_value(self, x):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            if n.nref is None:
                if x == n.data:
                    self.head = None
            else:
                print("node not present in list")
            if self.head.data == x:
                self.head = self.head.nref
                self.head.pref = None
            n = self.head
            while n.nref is not None:
                if x == n.data:
                    break
                n = n.nref
            if n.nref is not None:
                n.pref.nref = n.nref
                n.nref.pref = n.pref
            else:
                if n.data == x:
                    n.pref.nref = None
                else:
                    print("x is not present in the list")
DDL=double_LL()
DDL.add_end(10)
DDL.add_end(20)
DDL.add_end(30)
DDL.add_end(40)
DDL.add_end(50)
DDL.delete_begin()
DDL.delete_end()
DDL.delete_by_value(40)
DDL.print_double()
