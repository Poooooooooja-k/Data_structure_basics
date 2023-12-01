queue=[]
def enqueue():
    element=int(input("enter the element: "))
    queue.append(element)
    print(queue)
def dequeue():
    if queue is None:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("deleted element is :",e)
        print(queue)
def display():
    print(queue)
while True:
    print("select an option 1.push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice ==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("invalid choice")
    

