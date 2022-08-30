class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)+1):
            ans=ans^i
        for i in range(len(nums)):
            ans=ans^nums[i]
        return ans
        