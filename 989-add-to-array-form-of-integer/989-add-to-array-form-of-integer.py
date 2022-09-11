class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        temp=0
        for x in num:
            temp = (temp*10)+x
        temp+=k
        ans=[]
        while temp>0:
            rem=temp%10
            ans.append(rem)
            temp=temp//10
        l=0
        r=len(ans)-1
        while l<r:
            ans[l],ans[r]=ans[r],ans[l]
            l+=1
            r-=1
        return ans
        