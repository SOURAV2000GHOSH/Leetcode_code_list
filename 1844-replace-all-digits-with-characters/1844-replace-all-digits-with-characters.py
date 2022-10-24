class Solution:
    def replaceDigits(self, s: str) -> str:
        length=len(s)
        if length<2:
            return s
        l=0
        ans=[]
        while l<length:
            if l+1==length:
                ans.append(s[l])
            if l+1<length:
                ans.append(s[l])
                ans.append(chr(ord(s[l])+int(s[l+1])))
            l+=2
        return "".join(ans)
        