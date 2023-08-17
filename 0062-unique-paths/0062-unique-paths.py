class Solution:
    # def solve(self,i,j,dp):
    #     if i==0 and j==0:
    #         return 1
    #     if j<0 or i<0:
    #         return 0
    #     if dp[i][j]!=-1:
    #         return dp[i][j]
    #     up=self.solve(i-1,j,dp)
    #     upLeft=self.solve(i,j-1,dp)
    #     dp[i][j]=up+upLeft
    #     return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[-1 for i in range(n)] for j in range(m)]
        # return self.solve(m-1,n-1,dp)
        dp=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[0]=1
                else:
                    up=dp[j]
                    upLeft=0
                    if j>0:
                        upLeft=temp[j-1]
                    temp[j]=up+upLeft
            dp=temp
        return dp[n-1]
                