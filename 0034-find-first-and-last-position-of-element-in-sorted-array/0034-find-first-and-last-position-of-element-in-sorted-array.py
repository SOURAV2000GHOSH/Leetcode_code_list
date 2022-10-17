class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                ans[0],ans[1]=mid,mid
                r=mid-1
            if nums[mid]<target:
                l=mid+1
            if nums[mid]>target:
                r=mid-1
        if ans[1]>-1:
            while ans[1]<len(nums)-1 and nums[ans[1]+1]==target:
                ans[1]+=1
        return ans