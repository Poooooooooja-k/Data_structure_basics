class maxheap:
    def __init__(self) -> None:
        self.heap=[]
    def insert(self,element):
        self.heap.append(element)
        index=len(self.heap)-1
        self.heapify_up(index)
    def heapify_up(self,index):
        while index>0:
            parent_index = (index - 1) // 2
            if self.heap[index]>self.heap[parent_index]:
                self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
                index=parent_index
            else:
                break
    def delete(self):
        if self.heap is None:
            print("heap is empty")
        max_element=self.heap[0]
        last_element=self.heap.pop()
        if self.heap:
            self.heap[0]=last_element
            self.heapify_down(0)
        return max_element
    def heapify_down(self,index):
        while True:
            left_child_index=2*index+1
            right_child_index=2*index+2
            largest=index
            if left_child_index<len(self.heap) and self.heap[left_child_index]>self.heap[largest]:
                largest=left_child_index
            if right_child_index<len(self.heap) and self.heap[right_child_index]>self.heap[largest]:
                largest=right_child_index
            if largest!=index:
                self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
                index=largest
            else:
                break
m=maxheap()
elements=[4,10,3,5,1]
for element in elements:
    m.insert(element)
print(m.heap)
deleted_max = m.delete()
print("Deleted max element:", deleted_max)
print("Max-Heap after deletion:", m.heap)