class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        check=[[-1 for i in range(1000)] for i in range(1000)]
        def solve(i,j,m,n):
            if check[i][j]!=-1:
                return check[i][j]
            if i>=m or j>=n:
                return 0
            if text1[i]==text2[j]:
                check[i][j]=1+solve(i+1,j+1,m,n)
                return check[i][j]
            l= solve(i+1,j,m,n)
            r=solve(i,j+1,m,n)
            check[i][j]=max(l,r)
            return check[i][j]
        return  solve(0,0,len(text1),len(text2))
            
        