class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=len(s)
        ans=[""]*l
        index=0
        for i in indices:
            ans[i]=s[index]
            index+=1
        return "".join(ans)