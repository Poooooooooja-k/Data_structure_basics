def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
input_list=input("enter a list of space seperated elements:")
user_list=list(map(int,input_list.split()))
search_element=int(input("enter the element to search:"))
result=linear_search(user_list,search_element)
if result!= -1:
    print(f"element {search_element} found at index {result}")
else:
    print(f"element {search_element} not found")