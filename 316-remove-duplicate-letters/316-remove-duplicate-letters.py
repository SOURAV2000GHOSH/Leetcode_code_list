class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cheak=dict()
        ans=[]
        k=set()
        for indx,el in enumerate(s):
            cheak[el]=indx
        for index,el in enumerate(s):
            while len(ans)>0 and ans[-1]>el and cheak[ans[-1]]>index and el not in k:
                l=ans.pop()
                k.remove(l)
            if el not in k:
                ans.append(el)
                k.add(el)
        return "".join(ans)