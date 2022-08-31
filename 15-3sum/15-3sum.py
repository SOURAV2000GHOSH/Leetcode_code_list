class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        nums.sort()
        ans=[]
        for indx,el in enumerate(nums):
            if indx>0 and el==nums[indx-1]:
                continue
            left=indx+1
            right=l-1
            while left<right:
                three_sum=el+nums[left]+nums[right]
                if three_sum==0:
                    ans.append([el,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                if three_sum<0:
                    left+=1
                if three_sum>0:
                    right -= 1
        return ans