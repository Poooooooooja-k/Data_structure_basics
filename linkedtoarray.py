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
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def linked_to_array(self):
        array=[]
        if self.head is None:
            print("empty list")
        else:
            n=self.head
            while n is not None:
                array.append(n.data)
                n=n.ref
            return array
l=linked_list()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)
l.add_begin(40)
result=l.linked_to_array()
print(result)
