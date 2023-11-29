class Stacktoqueue:
    def __init__(self) -> None:
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("stack is empty")
    def stack_queue(self):
        queue=[]
        while self.stack:
            # pop elements from stack and append 
            queue.append(self.stack.pop())
        return queue
s=Stacktoqueue()
s.push(10)
s.push(20)
s.push(30)
queue=s.stack_queue()
print("queue is:",queue)
