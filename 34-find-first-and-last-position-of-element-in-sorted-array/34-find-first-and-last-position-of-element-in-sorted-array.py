class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        for x in range(len(nums)):
            if nums[x]==target:
                ans[0]=x
                break
        for x in range(len(nums)-1,-1,-1):
            if nums[x]==target:
                ans[1]=x
                break
        return ans