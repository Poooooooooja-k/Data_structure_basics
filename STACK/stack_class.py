class stack:
    def __init__(self) -> None:
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            print("list is empty")
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
    def print_stack(self):
        if not self.is_empty():
            print(self.stack)
        else:
            print("list is empty")
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.print_stack()
