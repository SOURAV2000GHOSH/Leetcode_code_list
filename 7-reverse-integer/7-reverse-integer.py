class Solution:
    def reverse(self, x: int) -> int:
        isnegative=1
        if x<0:
            isnegative =-1
        a=abs(x)
        ans=0
        while a>0:
            rem=a%10
            ans = (ans*10)+rem
            a=a//10
        ans =ans*isnegative
        if -2**31<ans<(2**31-1):
            return ans
        return 0
        
        