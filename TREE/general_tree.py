class general_tree:
    def __init__(self,key) -> None:
        self.key=key
        self.children=[]
    def insert(self,data):
        if self.key is None:
            self.key=data
        if self.key==data:
            return
        else:
            new_node=general_tree(data)
            self.children.append(new_node)
    def delete(self,target_key):
        new_children = []
        for child in self.children:
            if child.key != target_key:
                new_children.append(child)
            else:
                child.delete(target_key)
        self.children = new_children
    def print_tree(self):
        print(self.key, end=" ")
        for i in self.children:
            i.print_tree()
    def is_prime(self,n):
        if n<2:
            return False
        for i in range(2,int(n/2)):
            if n%i==0:
                return False
        return True
    def delete_prime(self):
        if self.key is None:
            return 
        self.children=[child for child in self.children if not child.is_prime(child.key)]
        return self.children
tree=general_tree(10)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(7)
target_key = 7
tree.delete(target_key)
tree.print_tree()
tree.delete_prime()
print()