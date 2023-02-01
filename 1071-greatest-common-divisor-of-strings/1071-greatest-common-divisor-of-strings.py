class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        def isGcdString(n):
            if l1%n or l2%n:
                return False
            f1,f2=l1//n,l2//n
            if str1[:n]*f1==str1 and str1[:n]*f2==str2:
                return True
        for i in range(min(l1,l2),0,-1):
            if isGcdString(i):
                return str1[:i]
        return ""
            