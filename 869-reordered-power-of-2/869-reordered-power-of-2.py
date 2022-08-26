from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a=Counter([int(x) for x in str(n)])
        temp,i=0,0
        
        while temp<=10**9:
            temp=2**i
            c=Counter([int(x) for x in str(temp)])
            if c==a:
                return True
            i+=1
        return False
            
        
        