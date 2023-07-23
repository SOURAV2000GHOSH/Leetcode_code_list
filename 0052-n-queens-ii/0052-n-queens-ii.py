class Solution:
    def traverse(self,col,n,board,ans,NEdiagonal,SEdiagonal,Erow):
        if col==n:
            ans[0]+=1
            return
        for row in range(n):
            if not Erow[row] and not NEdiagonal[(n-1)+(col-row)] and not SEdiagonal[row+col]:
                board[row][col]="Q"
                Erow[row]=True
                NEdiagonal[(n-1)+(col-row)]=True
                SEdiagonal[row+col]=True
                self.traverse(col+1,n,board,ans,NEdiagonal,SEdiagonal,Erow)
                Erow[row]=False
                NEdiagonal[(n-1)+(col-row)]=False
                SEdiagonal[row+col]=False
                board[row][col]="."
        
    def totalNQueens(self, n: int) -> List[List[str]]:
        NEdiagonal=[False]*((2*n)-1)
        SEdiagonal=[False]*((2*n)-1)
        Erow=[False]*n
        ans=[0]
        board=[["." for i in range(n)] for j in range(n)]
        self.traverse(0,n,board,ans,NEdiagonal,SEdiagonal,Erow)
        return ans[0]
        