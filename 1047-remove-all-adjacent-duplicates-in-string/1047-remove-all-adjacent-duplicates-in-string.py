class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]
        for x in s:
            if len(ans)!=0 and x ==ans[-1]:
                ans.pop()
            else:
                ans.append(x)
        return "".join(ans)
        