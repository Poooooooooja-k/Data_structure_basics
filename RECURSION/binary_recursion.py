def binary_search(list,element,lower,upper):
    if lower<=upper:
        mid=(lower+upper)//2
        if element==list[mid]:
            return mid 
        elif element<list[mid]:
            return binary_search(list,element,lower,mid-1)
        elif element>list[mid]:
            return binary_search(list,element,mid+1,upper)
    else:
        return -1
def search(list,element):
    list.sort()
    print(list)
    result=binary_search(list,element,0,len(list)-1)
    if result!=-1:
        print(f"element {element} found at position {result}")
    else:
        print("element not found")
list=[1,2,3,4,5,6,7,8,9,10]
element=int(input("enter the element to be found"))
search(list,element)