class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def search_island(i,j):
            q=collections.deque()
            q.append((i,j))
            direction=[(0,1),(0,-1),(1,0),(-1,0)]
            
            while q:
                temp_r,temp_c=q.popleft()
                for dr,dc in direction:
                    row=temp_r+dr
                    col=temp_c+dc
                    #r,c=row_size, col_size of grid that is mention below
                    if -1<row<r and -1<col<c and ((row,col) not in visit) and grid[row][col]=='1':
                        visit.add((row,col))
                        q.append((row,col))
                                 
        if not grid:
            return 0
        r,c=len(grid),len(grid[0])
        visit=set()
        island=0
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in visit and grid[i][j]=='1':
                    visit.add((i,j))
                    search_island(i,j)
                    island +=1
        return island
        
        