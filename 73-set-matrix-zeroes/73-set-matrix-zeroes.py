class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        
        # use for cheaking first row and column have have 0
        in_first_row,in_first_col=False,False 
        #cheaking first row and column have 0
        for j in range(n):
            if matrix[0][j]==0:
                in_first_row=True
                break
        for i in range(m):
            if matrix[i][0]==0:
                in_first_col=True
                break
        #making first row and first column point to be zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        #making whole row and col to be 0 that is pointed 
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0
        #if in first row and first col have 0 then make whole first col and row to be 0
        if in_first_row:
            for j in range(n):
                matrix[0][j]=0
        if in_first_col:
            for i in range(m):
                matrix[i][0]=0
                    
        