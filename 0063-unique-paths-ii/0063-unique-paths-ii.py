class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return 0
        m=len(grid)
        n=len(grid[0])
        dp=[0]*n
        for i in range(m):
            temp=[0]*n
            for j in range(n):
                if i==0 and j==0:
                    temp[0]=1
                else:
                    if grid[i][j]==1:
                        temp[j]=0
                        continue
                    up=dp[j]
                    left=0
                    if j>0:
                        left=temp[j-1]
                    temp[j]=up+left
            dp=temp
        return dp[n-1]
                    
        