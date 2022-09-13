class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums.sort()
        l=0
        r=len(nums)-1
        if nums[r]!=nums[r-1]:
            return nums[r]
        if nums[l] != nums[l+1]:
            return nums[l]
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid-1] != nums[mid] != nums[mid+1]:
                return nums[mid]
            if (nums[mid]!=nums[mid+1] and mid%2==1) or (mid%2==0 and nums[mid] != nums[mid-1]):
                l=mid+1
            else:
                r=mid-1
            