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
    def delete_by_value(self, x):
        n = self.head
        if n is None:
            print("empty")
        else:
            if self.head.data == x:
                self.head = self.head.ref
            else:
                while n.ref is not None:
                    if n.ref.data == x:
                        break
                    else:
                        n = n.ref
                if n is None:
                    print("empty linkedlist")
                else:
                    n.ref = n.ref.ref
LL1=linked_list()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.delete_by_value(30)
LL1.print_LL()
            



