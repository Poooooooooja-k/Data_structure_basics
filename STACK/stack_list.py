stack=[]
def push():
    if len(stack)==n:
        print("list is full")
    else:
        element=int(input("enter the element: "))
        stack.append(element)
        print(stack)
def pop():
    if stack is None:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element: ",e)
        print(stack)
n=int(input("enter limit of stack: "))
while True:
    print("select an option 1.push 2.pop 3.quit:")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("invalid choice")
