class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        a=[True]*n
        a[0],a[1]=False,False
        i=0
        while i<sqrt(n):
            if a[i]==True:
                for j in range(i*i,n,i):
                    a[j]=False
                    
            i +=1
        
        return a.count(True)
            
                    
        