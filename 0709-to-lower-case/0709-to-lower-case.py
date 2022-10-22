class Solution:
    def toLowerCase(self, s: str) -> str:
        l=0
        ans=[]
        while l<len(s):
            temp= ord(s[l])
            if 65<= temp <=90:
                ans.append(chr(temp+32))
                l+=1
                continue
            ans.append(s[l])
            l+=1
        return "".join(ans)
        