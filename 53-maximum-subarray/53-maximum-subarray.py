class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        maxsum=nums[0]
        for x in nums:
            cursum += x
            if maxsum < cursum:
                maxsum = cursum
            if cursum < 0:
                cursum = 0
        return maxsum
            
        