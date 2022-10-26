class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        p=0
        
        while c<len(s) and p<len(t):
            if s[c]==t[p]:
                c+=1
            p+=1
        if c<len(s):
            return False
        return True
        