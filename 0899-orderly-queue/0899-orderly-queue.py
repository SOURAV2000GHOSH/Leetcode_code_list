class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1:
            ans=s
            for x in range(len(s)-1):
                s=s[1:]+s[0]
                ans=min(ans,s)
            return ans
        else:
            return "".join(sorted(s))
        