class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l=len(nums)
        right=[0]*l
        left=[0]*l
        rightSum=0
        leftSum=0
        for i in range(l):
            left[i]=leftSum
            leftSum+=nums[i]
            right[l-i-1]=rightSum
            rightSum+=nums[l-i-1]
        ans=[0]*l
        for i in range(l):
            if left[i]<=right[i]:
                ans[i]=right[i]-left[i]
            else:
                ans[i]=left[i]-right[i]
        return ans
            
        