class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n<=2:
            return True
        temp=n%2
        n=n//2
        while n>0:
            rem=n%2
            if temp == rem:
                return False
            temp=rem
            n=n//2
        return True
        
        