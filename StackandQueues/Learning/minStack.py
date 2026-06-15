class SpecialStack:

    def __init__(self):
        # Define Stack
        self.s = []
        
    
    def push(self, x):
        # Add an element to the top of Stack
        if len(self.s) == 0:
            self.s.append([x,x])
        else:
            mini = min(self.s[-1][1],x)
            self.s.append([x,mini])
            
    
    def pop(self):
        # Remove the top element from the Stack
        if len(self.s) == 0:
            return None
        return self.s.pop()
        

    
    def peek(self):
        # Returns top element of Stack
        if len(self.s) == 0:
            return -1
        return self.s[-1][0]
        
    def isEmpty(self):
        # Check if the stack is empty
        if len(self.s) == 0:
            return True
        return False
    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.s) == 0:
            return - 1
        return self.s[-1][1]
        
        
        
        