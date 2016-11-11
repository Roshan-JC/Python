class Queue:
    
    def __init__(self,size):
        self._data = []
        self.size = size
        
        
    def is_empty(self):
        return len(self._data)==0
    
    def enqueue(self,e):
        if(len(self._data)>= self.size   ):
            print("over flow")
        else:
            self._data.insert(0,e)
        
    def dequeue(self):
        if(self.is_empty()):
            print ("stack empty")
        else:
            return self._data.pop()
        
    def display(self):
        print(self._data)
        
    def repop(self):
        b.enqueue(a.dequeue())
    
    
        
if __name__ == '__main__':
    
    a = Queue(5)
    b = Queue(5)
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)
    a.display()
    b.repop()
    b.repop()
    b.display()
    
    
    

    
    
    
    
    
  
    
