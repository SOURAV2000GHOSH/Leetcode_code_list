class MyQueue:

    def __init__(self):
        self.stack=[]
        self.top=-1
        self.buttom=-1
        

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        self.top=len(self.stack)-1
        if self.top==0:
            self.buttom=0
        

    def pop(self) -> int:
        ans=self.stack[self.buttom]
        self.buttom+=1
        if self.buttom>self.top:
            self.stack.clear()
            self.top=self.buttom=-1
        return ans
        
        
        

    def peek(self) -> int:
        return self.stack[self.buttom]
        

    def empty(self) -> bool:
        if self.buttom==-1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()