class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)-1
        ans=[0]*(l+1)
        check=[]
        
        for i in range(l,-1,-1):
            while len(check)>0 and temperatures[check[-1]]<=temperatures[i]:
                check.pop()
            if len(check)==0:
                ans[i]=0
            else:
                ans[i]=check[-1]-i
            check.append(i)
        return ans
                