class Solution:
    def isSafe(self,row,col,board):
        ch=board[row][col]
        for i in range(9):
            if board[row][i]==ch:
                if col==i:
                    continue
                return False
            if board[i][col]==ch:
                if row==i:
                    continue
                return False
            tempRow=(3*(row//3))+(i//3)
            tempCol=(3*(col//3))+(i%3)
            if board[tempRow][tempCol]==ch:
                if row==tempRow and col==tempCol:
                    continue
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if not self.isSafe(row,col,board):
                        print(row,col)
                        return False
        return True
        