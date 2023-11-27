# ascending order
def bubble(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            # for descending order change > to <
            if list[j]>list[j+1]:       
                list[j],list[j+1]=list[j+1],list[j]
    return list
list1=[10,25,4,23,0]
print(list1)
bubble(list1)
print("sorted list :",list1)
            