class MinStack:

    def __init__(self):
        self.A=[]
        

    def push(self, x: int) -> None:
        self.A.insert(0, x)
        

    def pop(self) -> None:
        self.A.pop(0)
        

    def top(self) -> int:
        return self.A[0]
        

    def getMin(self) -> int:
        min1 = 99999999999999999999999
        for i in range(len(self.A)):
            if(min1>self.A[i]):
                min1 = self.A[i]
        return min1
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
