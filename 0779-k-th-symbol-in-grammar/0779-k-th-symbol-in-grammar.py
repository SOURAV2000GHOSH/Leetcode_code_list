class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k==1:
            return 0
        temp=1
        # if k%2==0:
        #     temp=self.kthGrammar(n-1,k//2)
        # else:
        #     temp=self.kthGrammar(n-1,(k//2)+1)
        
        if k<=(2**(n-1)//2):
            temp=self.kthGrammar(n-1,k)
        else:
            temp=0 if self.kthGrammar(n-1,k-(2**(n-1)//2))==1 else 1
            
        # if temp==0:
        #     if k%2==1:
        #         return 0
        #     else:
        #         return 1
        # else:
        #     if k%2==1:
        #         return 1
        #     else:
        #         return 0
        
        return temp