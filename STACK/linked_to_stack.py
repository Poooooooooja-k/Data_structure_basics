class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def add(self,data):
        n=self.head
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def linked_to_stack(l):
        stack=[]
        n=l.head
        while n:
            stack.append(n.data)
            n=n.ref
        return stack
l=linked_list()
l.add(10)
l.add(20)
l.add(30)
s=l.linked_to_stack()
print(s)
