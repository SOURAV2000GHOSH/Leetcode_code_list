class Solution:
    def isSafe(self,row,col,board,n):
        drow=row
        dcol=col
        while drow>=0 and dcol>=0:
            if board[drow][dcol]=="Q":
                return False
            drow-=1
            dcol-=1
        drow=row
        dcol=col
        while drow>=0 and dcol>=0:
            if board[drow][dcol]=="Q":
                return False
            dcol-=1
        drow=row
        dcol=col
        while n>drow>=0 and dcol>=0:
            if board[drow][dcol]=="Q":
                return False
            drow+=1
            dcol-=1
        return True
    
    def traverse(self,col,n,board,ans):
        if col==n:
            ans[0]+=1
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]="Q"
                self.traverse(col+1,n,board,ans)
                board[row][col]="."
        
    def totalNQueens(self, n: int) -> List[List[str]]:
        ans=[0]
        board=[["." for i in range(n)] for j in range(n)]
        self.traverse(0,n,board,ans)
        return ans[0]
        