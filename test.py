class max_heap:
    def __init__(self) -> None:
        self.heap=[]
    def insert(self,element):
        self.heap.append(element)
        index=len(self.heap)-1
        self.heapify_up(index)
    def heapify_up(self,index):
        while index>0:
            parent_index=[index-1]//2
            if self.heap[index]>self.heap[parent_index]:
                self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
                
