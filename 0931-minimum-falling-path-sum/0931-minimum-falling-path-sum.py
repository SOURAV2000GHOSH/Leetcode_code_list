
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        t=[[0 for i in range(n)] for i in range(n)]
        for col in range(n):
            t[0][col]=matrix[0][col]
        for row in range(1,n):
            for col in range(n):
                if col+1<n:
                    t[row][col]=matrix[row][col]+min(t[row-1][col],t[row-1][col+1])
                if col-1>=0:
                    t[row][col]=matrix[row][col]+min(t[row-1][col-1],t[row-1][col])
                if col+1<n and col-1>=0:
                    t[row][col]=matrix[row][col]+min(t[row-1][col-1],t[row-1][col],t[row-1][col+1])
        minSum=100000000000000
        for col in range(n):
            minSum=min(minSum,t[n-1][col])
        return minSum