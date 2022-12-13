
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        cheak=[[-1 for x in range(101)] for i in range(101)]
        def solve(matrix,row,col,n):
            if cheak[row][col]!=-1:
                return cheak[row][col]
            if row==(n-1):
                return matrix[row][col]
            min_val=1000000000000000
            total=matrix[row][col]
            for shift in [-1,0,1]:
                if row+1<n and 0<=col+shift<n:
                    min_val=min(min_val,total+solve(matrix,row+1,col+shift,n))
            # if row+1<n and col-1>=0:
            #     min_val=min(min_val,total+solve(matrix,row+1,col-1,n)) 
            # if row+1<n:
            #     min_val=min(min_val,total+solve(matrix,row+1,col,n))
            # if row+1<n and col+1<n:
            #     min_val=min(min_val,total+solve(matrix,row+1,col+1,n))
            cheak[row][col]=min_val
            return min_val
        minSum=10000000000000000000
        for i in range(n):
            minSum=min(minSum,solve(matrix,0,i,n))
        return minSum