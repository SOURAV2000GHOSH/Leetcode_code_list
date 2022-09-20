class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for x in sentences:
            l=len(x.split())
            if ans<l:
                ans=l
        return ans
        