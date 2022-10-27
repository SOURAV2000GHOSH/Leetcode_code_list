class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cheak=dict()
        for x in nums:
            cheak[x]=1 if x not in cheak else cheak[x]+1
        ans=0
        for x in cheak.keys():
            if cheak[x]==1:
                ans += x
        return ans
        