class Hashtable:
    def _init_(self,size):
        self.size=size
        self.table=[None]*size
    def hashfunction(self,key):
        return key %self.size
    def hashfunction2(self,key):
        return 7-(key %7)
    def insert(self,key,value):
        index=self.hashfunction(key)
        if self.table[index] is None:
            self.table[index]=(key,value)
        else:
            index1=index
            i=1
            while i<self.size:
                index1=(index+i*self.hashfunction2(key))%self.size
                if self.table[index1] is None:
                    self.table[index1]=(key,value)
                i+=1
                if i==self.size:
                    break
    def search(self,key):
        index=self.hashfunction(key)
        if self.table[index][0]==key:
            return self.table[index][1]
        else:
            i=1
            index1=index
            while i<self.size:
                index1=(index+i*self.hashfunction2(key))%self.size
                if self.table[index][0]==key:
                    return self.table[index][1]
                i+=1
                if i==self.size:
                    break
    def display(self):
        for item in self.table:
            while item:
                print({item[0]:item[1]})
                break
            print("none")
h=Hashtable(10)
h.insert(1,"oarnhe")
h.display()