class Solution:
    def makeGood(self, s: str) -> str:
        
        for l in range(len(s)) :
            if l<len(s)-1 and abs(ord(s[l+1])-ord(s[l]))==32:
                return self.makeGood(s[:l]+s[l+2:])  
        return s