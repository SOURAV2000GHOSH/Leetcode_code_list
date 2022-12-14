class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums,n,i,check):
            
            if i>=n:
                return 0
            if check[i]!=-1:
                return check[i]
            thief=nums[i]+solve(nums,n,i+2,check)
            skip=solve(nums,n,i+1,check)
            check[i]=max(thief,skip)
            return check[i]
        n=len(nums)
        check=[-1]*n
        return solve(nums,n,0,check)
        
        