class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strat=len(s)
        for x in range(len(s)-1,-1,-1):
            if s[x]==" ":
                continue
            start=x
            break
        ans=0
        for x in range(start,-1,-1):
            if s[x]==' ':
                break
            ans +=1
        return ans