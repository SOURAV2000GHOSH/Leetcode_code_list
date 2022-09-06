class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        r=len(nums)-1
        if nums[0]!=nums[1]:
            return nums[0]
        elif nums[r]!=nums[r-1]:
            return nums[r]
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]!=nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (nums[mid]==nums[mid+1] and mid%2==0)or(nums[mid]==nums[mid-1] and mid%2==1):
                l=mid+1
            else:
                r=mid-1
            
        return -1