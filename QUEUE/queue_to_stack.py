class Queuetostack:
    def __init__(self) -> None:
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
    def queue_stack(self):
        stack=[]
        if self.queue:
            stack.extend(self.queue)
        return stack
q=Queuetostack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
stack=q.queue_stack()
print(stack)
