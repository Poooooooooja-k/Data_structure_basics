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
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
    def search(self,data):
        if self.key==data:
            print("node is found!!")
            return
        if data<self.key:
            if self.lchild:
                    self.lchild.search(data)
            else:
                print("node is not found!!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node not found!!")
    def delete(self,data):
        if self.key is None:
            print("tree is empty!!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("node not present")
        elif data>self.key:
            if self.rchild:
                self.rchild.delete(data)
            else:
                print("node not present")
        else:
            
            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            successor = self.rchild
            while successor and successor.lchild:
                successor = successor.lchild

            if successor:
                # Copy the inorder successor's key to this node
                self.key = successor.key

                # Delete the inorder successor
                self.rchild = self.rchild.delete(successor.key)
            else:
                # If successor is None, just set the node to None
                return None
        return self
root=BST(10)
list1=[20,4,30,4,1,5,6]
for i in list1:
    root.insert(i)
root.search(6)
root.delete(6)
