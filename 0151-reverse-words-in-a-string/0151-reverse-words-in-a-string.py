class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        cheak=set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        l=len(s)
        i=l-1
        while True:
            if s[i] not in cheak:
                i-=1
            break
        j=None
        while i>-1:
            if s[i] not in cheak:
                i-=1
                continue
            j=i+1
            while True:
                if i>-1 and s[i] in cheak:
                    i-=1
                    continue
                break
            ans.append(s[i+1:j])
            
        return " ".join(ans)