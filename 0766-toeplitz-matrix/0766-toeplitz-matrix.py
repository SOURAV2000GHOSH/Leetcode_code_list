class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                prev=matrix[i-1][j-1]
                cur=matrix[i][j]
                if cur==prev:
                    continue                     
                return False
        return True
        