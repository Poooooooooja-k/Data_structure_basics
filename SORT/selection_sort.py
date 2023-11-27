# using in-built function min()
# ascending order
# code for descending change the min() to max() and also change the variable names
list1=[56,0,2,2,6,0]
print(list1)
for i in range(len(list1)-1):
    # only consider the unsorted part of th list 
    min_value = min(list1[i:])     
    min_ind=list1.index(min_value,i)
    # when 2 same elements come 
    if list1[i]!=list1[min_ind]:
        list1[i],list1[min_ind]=list1[min_ind],list1[i]
print("sorted list:",list1)