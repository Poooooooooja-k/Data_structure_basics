class BST:
    def __init__(self,key) -> None:
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        if self.key<data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print("node is found")
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not found")
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
root=BST(10)
list1=[6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
print("pre-order")
root.preorder()
print()
print("inorder")
root.inorder()
print()
print("postorder")
root.postorder()
print()
        