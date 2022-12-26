class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if x<=i+nums[i]:x=i
        return x==0