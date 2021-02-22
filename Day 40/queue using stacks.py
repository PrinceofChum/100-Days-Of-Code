# Python3 program to implement Queue using   
# one stack and recursive call stack.  
class Queue: 
    def __init__(self): 
        self.s = []      
    # Enqueue an item to the queue  
    def enQueue(self, data): 
        self.s.append(data) 
        
    # Dequeue an item from the queue  
    def deQueue(self): 
        # Return if queue is empty 
        if len(self.s) <= 0: 
            print('Queue is empty') 
            return
        # pop an item from the stack 
        x = self.s[len(self.s) - 1] 
        self.s.pop()   
        # if stack become empty 
        # return the popped item 
        if len(self.s) <= 0: 
            return x       
        # recursive call 
        item = self.deQueue()   
        # push popped item back to 
        # the stack 
        self.s.append(x) 
          
        # return the result of  
        # deQueue() call 
        return item 
      
# Driver code   
if __name__ == '__main__': 
    q = Queue() 
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
      
    print(q.deQueue()) 
    print(q.deQueue()) 
    print(q.deQueue())
