class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        temp=s.split(' ')
        for x in temp:
            temp2=list(x)
            l=0
            r=len(temp2)-1
            while l<r:
                temp2[l],temp2[r]=temp2[r],temp2[l]
                l+=1
                r-=1
            ans.append(''.join(temp2))
        return " ".join(ans)