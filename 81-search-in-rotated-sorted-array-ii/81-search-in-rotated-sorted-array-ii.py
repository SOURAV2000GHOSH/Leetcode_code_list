class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            if nums[mid]<target:
                l=mid+1
            if nums[mid]>target:
                r=mid-1
        return False
        