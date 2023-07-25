class Solution:
    def isSafe(self,Grow,Gcol,board,ch):
        for i in range(0,9):
            if board[Grow][i]==ch:
                return False
            if board[i][Gcol]==ch:
                return False
            if board[(3*(Grow//3))+(i//3)][(3*(Gcol//3))+(i%3)]==ch:
                return False
        return True
            
    def solve(self,board):
        for row in  range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==".":
                    for i in range(1,10):
                        if self.isSafe(row,col,board,str(i)):
                            board[row][col]=str(i)
                            if self.solve(board):
                                return True
                            else:
                                board[row][col]="."
                    return False
        return True
                        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        