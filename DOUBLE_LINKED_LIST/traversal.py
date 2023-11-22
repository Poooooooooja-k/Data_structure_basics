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
    def double_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data)
                n=n.pref
DDL=double_ll()
DDL.print_double()
DDL.double_reverse()
