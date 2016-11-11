class stack:
    
    def __init__(self):
        self._data = []
        
    def isempty(self):
        return len(self._data)== 0
    
    def push(self, x):
        self._data.append(x)
        
    def pop(self):
        if self.isempty():
            print("empty")
        else:
            return self._data.pop()
            
    def display(self):
        print(self._data)
        
    def stackt(self,t):
        length = len(self._data)
        for i in range(length):
            t.push(self.pop())
        

if __name__ == '__main__':

    s = stack()
    t = stack()

    s.push(9)
    
    s.push(5)
    s.push(4)
    s.display()
    s.stackt(t)
    
    
    
    t.display()

