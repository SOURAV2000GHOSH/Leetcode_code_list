class Solution:
    def countSegments(self, s: str) -> int:
        l=len(s)
        x=0
        count=0
        isWord=True
        while x<l:
            if isWord and s[x] != " ":
                count+=1
                isWord=False
            if s[x]==" ":
                isWord=True
            x+=1
        return count
        