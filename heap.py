
class Heap :
    def __init__(self) -> None:
        self.heaparray=[]
    
    def get(self):
        return self.heaparray
    def parent(self,pos):

        if (pos-1)/2>=0:
            return int((pos-1)/2)
        
        return 0

    def leftChild(self, pos):
         if (2*pos+1)>0:
            return 2*pos+1
        
         return 0

    def rightChild(self, pos):
         if (2*pos+2)>0:
            return 2*pos+2
        
         return 0
    def heapify(self,pos):
        while (pos >0 and (self.heaparray[pos] > self.heaparray[self.parent(pos)])):
            self.heaparray[pos] , self.heaparray[self.parent(pos)] = self.heaparray[self.parent(pos)] ,self.heaparray[pos]
            pos = self.parent(pos)

    def insert(self,key):
        if len(self.heaparray) ==0:
            self.heaparray.append(key)
            return
        pos = len(self.heaparray)
        self.heaparray.append(key)
        self.heapify(pos)

    def getMax(self):
        if len(self.heaparray) ==0:
            return -1
        return self.heaparray[0]
    
    def pop(self):
        if len(self.heaparray) ==0:
            return -1
        ans = self.heaparray[0]
        self.heaparray[0] = self.heaparray.pop()
        self.maxHeapify(0)
        return ans
        
    def maxHeapify(self,pos):
        l = self.leftChild(pos)
        r = self.rightChild(pos)
        largest = pos
        if (l< len(self.heaparray) and self.heaparray[l] > self.heaparray[largest]):
            largest = l
        if r < len(self.heaparray) and self.heaparray[r] > self.heaparray[largest]:
            largest = r

        if largest != pos:
            self.heaparray[largest] , self.heaparray[pos] = self.heaparray[pos] ,self.heaparray[largest] 
            self.maxHeapify(largest)

obj = Heap()
obj.insert(3)
obj.insert(2)
obj.insert(6)
obj.insert(8)
obj.insert(1)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.get())