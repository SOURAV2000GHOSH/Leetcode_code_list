class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prev=self.countAndSay(n-1)
        
        ans=[]
        l=len(prev)
        count=0
        start=0
        for start in range(l):
            count+=1
            if start==(l-1) or prev[start]!=prev[start+1]:
                ans.append(str(count))
                ans.append(prev[start])
                count=0
                
    
        return "".join(ans)
        
            
            
        