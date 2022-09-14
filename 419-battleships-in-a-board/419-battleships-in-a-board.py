class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        r=len(board)
        c=len(board[0])
        ans=0
        for i in range(r):
            for j in range(c):
                if board[i][j]=='X':
                    if 0<=(i-1)<r and board[i-1][j]=='X':
                        continue
                    if 0<=(j-1)<c and board[i][j-1]=="X":
                        continue
                    ans +=1
        return ans