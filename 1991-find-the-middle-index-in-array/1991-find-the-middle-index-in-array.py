class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        tempSum=0
        for i in range(len(nums)):
            if(i==0):
                if (tempSum)==(s-nums[i]-tempSum):
                    return i
                continue
            tempSum+=nums[i-1]
            if (tempSum)==(s-nums[i]-tempSum):
                return i
        return -1
        