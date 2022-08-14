class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)==1:
        #     return False
        b={")":"(","}":"{","]":"["}
        a=[]
        for x in s:
            if x=="(" or x=="{" or x=="[":
                a.append(x)
            elif len(a)>0 and b[x]==a[-1]:
                a.pop()
            else:
                return False
        if len(a)>0:
            return False
        return True
        