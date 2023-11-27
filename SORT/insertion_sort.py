def insertionsort(list):
    for i in range(1,len(list)):
        current_element=list[i]
        pos=i
        while current_element<list[pos-1] and pos>0:
            list[pos]=list[pos-1]
            pos=pos-1
        list[pos]=current_element
list1=[2,4,3,5,1]
insertionsort(list1)
print(list1)