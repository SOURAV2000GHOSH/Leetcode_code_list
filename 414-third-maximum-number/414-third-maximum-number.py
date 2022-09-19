class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        ans=nums[-1]
        cheak=2
        l=len(nums)-2
        while l>-1:
            if cheak==0:
                break
            if nums[l]<ans:
                ans=nums[l]
                cheak-=1
            l-=1
        if cheak==0:
            return ans
        return nums[-1]