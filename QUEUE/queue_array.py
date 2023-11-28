class queue:
    def __init__(self) -> None:
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.queue is None:
            print("queue is empty")
        else:
            self.queue.pop(0)
    def empty(self):
        return len(self.queue)==0
    def front(self):
        if self.queue is not None:
            print("deleting from 1st",self.queue[0])
    def rear(self):
        if self.queue is None:
            print("queue is empty")
        else:
            print("inseritng last",self.queue[-1])
    def size(self):
        return len(self.queue)
    def display(self):
        print(self.queue)
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
length=q.size()
print(length)
q.front()
q.rear()
q.dequeue()
q.display()
