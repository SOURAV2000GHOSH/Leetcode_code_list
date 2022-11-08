class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        l=1
        r=1
        while r<len(nums):
            if nums[r] != nums[r-1]:
                nums[l]=nums[r]
                l += 1
                r += 1
            else:
                r += 1
        return l
            