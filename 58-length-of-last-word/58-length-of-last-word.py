class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=len(s)
        cheak=set("abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        ans=0
        for x in range(l-1,-1,-1):
            if s[x]==' ':
                break
            ans +=1
        return ans