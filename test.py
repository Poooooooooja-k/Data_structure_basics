def insertion(list1):
    for i in range(len(list1)):
        current_element=list1[i]
        pos=i
        while current_element<list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion(my_list)
print(my_list)