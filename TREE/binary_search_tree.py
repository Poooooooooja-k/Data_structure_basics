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
    def delete(self, data):
        if self.key is None:
            print("Tree is empty!!")
            return self

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node not present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node not present")
        else:
            if self.lchild is None:
                return self.rchild
            elif self.rchild is None:
                return self.lchild

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
    def inorder_traversal(self):
        if self.lchild:
            self.lchild.inorder_traversal()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder_traversal()
    def min_key(self):
        current=self
        while current.lchild:
            current=current.lchild
        print("node with mininum key is:",current.key)
    def max_key(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with maximum key is:", current.key)
    def isbst(self):
        if self.key is not None:
            left=self.lchild is None or(self.lchild.key<self.key and self.lchild.isbst())
            right=self.rchild is None or(self.rchild.key>self.key and self.rchild.isbst())
            return left and right
        else:
            return True
    def closest_value(self,target):
        closest=self.key
        current=self
        while current:
            if abs(current.key-target)<abs(closest-target):
                closest=current.key
            if target<current.key:
                current=current.lchild
            elif target>current.key:
                current=current.rchild
            else:
                break
        return closest
root=BST(10)
list1=[20,4,30,1,5,6]
for i in list1:
    root.insert(i)
root.search(6)
print("\nInorder traversal after deletion:")
root.inorder_traversal()
root.max_key()
root.min_key()
is_bst = root.isbst()
print("Is it a BST?", is_bst)
target=10
result=root.closest_value(target)
print("closest to target:",result)