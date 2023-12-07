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
    def print_tree(self):
        print(self.key, end=" ")
        for i in self.children:
            i.print_tree()
tree=general_tree(10)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(70)
tree.print_tree()