class Solution:
    def isSafe(self,row,col,board,n,NEdiagonal,SEdiagonal,Erow):
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
    
    def traverse(self,col,n,board,ans,NEdiagonal,SEdiagonal,Erow):
        if col==n:
            temp=[]
            for el in board:
                temp.append("".join(el))
            ans.append(temp)
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
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        NEdiagonal=[False]*((2*n)-1)
        SEdiagonal=[False]*((2*n)-1)
        Erow=[False]*n
        ans=[]
        board=[["." for i in range(n)] for j in range(n)]
        self.traverse(0,n,board,ans,NEdiagonal,SEdiagonal,Erow)
        return ans
        