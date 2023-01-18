class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #for getting max sum
        def kadensMaxSum(arr):
            
            s=arr[0]
            maxSum=arr[0]
            for n in range(1,len(arr)):
                i=arr[n]
                s=max(s+i,i)
                maxSum=max(s,maxSum)
            return maxSum
        #fro getting min sum
        def kadensMinSum(arr):
            s=arr[0]
            minSum=arr[0]
            for n in range(1,len(arr)):
                i=arr[n]
                s=min(s+i,i)
                minSum=min(s,minSum)
            return minSum
        
        Sum=sum(nums)
        maxSum=kadensMaxSum(nums)
        minSum=kadensMinSum(nums)
        circularSum=Sum-minSum
        if maxSum>0:
            return max(maxSum,circularSum)
        return maxSum
        