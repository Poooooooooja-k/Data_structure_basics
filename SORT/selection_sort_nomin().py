def selection_sort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min]:
                min=j
        list1[i],list1[min]=list1[min],list1[i]
    return list1
list1=[45,87,98,23,13,12,11]
print(list1)
res=selection_sort(list1)
print("sorted array is:",list1)
