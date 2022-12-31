class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*l
        for i in range(l):
            ans[i]=nums[nums[i]]
        return ans