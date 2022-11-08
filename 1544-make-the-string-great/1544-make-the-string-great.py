class Solution:
    def makeGood(self, s: str) -> str:
        ans=[]
        for x in range(len(s)):
            if len(ans)>0 and abs(ord(ans[-1])-ord(s[x]))==32:
                ans.pop()
            else:
                ans.append(s[x])
        return "".join(ans)