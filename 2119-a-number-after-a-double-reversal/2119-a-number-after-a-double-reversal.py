class Solution:
    def reversal(self,n):
        ans=0
        while n>0:
            rem=n%10
            ans= (ans*10)+rem
            n=n//10
        return ans
    
    def isSameAfterReversals(self, num: int) -> bool:
        a=self.reversal(num)
        b=self.reversal(a)
        if b!=num:
            return False
        return True
        
        