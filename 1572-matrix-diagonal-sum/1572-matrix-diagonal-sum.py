class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        ans=0
        for i in range(n):
            ans+=mat[i][i]
        if n%2==0:
            for i in range(n):
                x=i
                y=n-1-i
                ans+=mat[x][y]
        else:
            for i in range(n):
                x=i
                y=n-1-i
                if x==y:
                    continue
                ans+=mat[x][y]
        return ans