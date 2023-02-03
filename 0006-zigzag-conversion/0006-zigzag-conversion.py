class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n=len(s)
        ans=[]
        for i in range(numRows):
            if i==0 or i==(numRows-1):
                l=i
                while l<n:
                    ans.append(s[l])
                    l+=((numRows-1)*2)
            else:
                l=i
                isFirst=True
                while l<n:
                    ans.append(s[l])
                    if isFirst:
                        l+=((numRows-i-1)*2)
                        isFirst=False
                    else:
                        l+=(i*2)
                        isFirst=True
        return "".join(ans)