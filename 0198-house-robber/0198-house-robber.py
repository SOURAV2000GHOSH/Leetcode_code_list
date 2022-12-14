class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        t=[0]*(n+1)
        t[1]=nums[0]
        for i in range(2,(n+1)):
            theft=nums[i-1]+t[i-2]
            skip=t[i-1]
            t[i]=max(theft,skip)
        return t[-1]
        
        