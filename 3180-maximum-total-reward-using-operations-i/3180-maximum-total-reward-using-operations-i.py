class Solution:
    def function(self,ind,n,reward,arr,dp):
        if(ind>=n):
            return 0
        if(dp[ind][reward]!=-1):
            return dp[ind][reward]
        a=0;
        if(arr[ind]>reward):
            a=arr[ind]+self.function(ind+1,n,arr[ind]+reward,arr,dp)
        b=0+self.function(ind+1,n,reward,arr,dp)
        dp[ind][reward] = max(a,b)
        return dp[ind][reward]
    
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        n=len(rewardValues)
        dp=[[-1 for j in range(10000)] for i in range(n)]
        rewardValues.sort()
        return self.function(0,n,0,rewardValues,dp)