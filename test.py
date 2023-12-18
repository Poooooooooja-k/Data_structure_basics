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
    def delete(self,target):
        new=[]
        for child in self.children:
            if child.key!=target:
                new.append(child)
            else:
                child.delete(target)
        self.children=new
    def print_tree(self):
        print(self.key,end=" ")
        for i in self.children:
            i.print_tree()
t=general_tree(10)
t.insert(20)
t.insert(30)
t.insert(1)
t.insert(2)
target=20
t.delete(target)
t.print_tree()