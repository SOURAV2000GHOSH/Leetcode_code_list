class Solution:
    def myAtoi(self, s: str) -> int:
        Min_int=-2**31
        Max_int=2**31-1
        ans=0
        i=0
        isnegative=1
        
        #white space
        while i<len(s) and s[i]==' ':
            i +=1
            
        #-/+ cheak
        if i<len(s) and (s[i]=='-'or s[i]=='+'):
            if s[i]=='-':
                isnegative=-1
            i+=1
        
            
        #cheak 0-9
        cheak=set("1234567890")
        while i<len(s) and s[i] in cheak:
            ans = (ans*10) + int(s[i])
            i+=1
        #cheak Min/Max int
        ans=isnegative*ans
        if ans<0:
            return max(Min_int,ans)
        return min(Max_int,ans)