def binary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        mid_element=arr[mid]
        if mid_element==target:
            return mid
        elif mid_element<target:
            low=mid+1
        else:
            high=mid-1
    return -1
input_list = input("Enter the list of space-separated numbers: ")    #split the input string into a list of strings and then convert each string to an integer.
unsorted_list = list(map(int, input_list.split()))
search_element=int(input("enter the element you want to search"))
sorted_list=sorted(unsorted_list)
result=binary_search(sorted_list,search_element)
if result!=-1:
    print(f"element {search_element} found at position {result}")
else:
    print(f"element {search_element} not found in list")