class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def array_to_link(self,array):
        if not array:
            return None
        else:
            new_node=Node(array[0])
            self.head=new_node
            n=self.head
            for i in range(1,len(array)):
                new_node=Node(array[i])
                n.ref=new_node
                n=new_node
                array_link=self.head
                while array_link is not None:
                    array_link=array_link.ref
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
l=linked_list()
array=[1,2,3,4,5]
l.array_to_link(array)
l.print_LL()