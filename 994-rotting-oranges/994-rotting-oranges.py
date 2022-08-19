class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        count=0
        q=deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.appendleft((i,j,0))
                if grid[i][j]==1:
                    count +=1
        if count==0:
            return count
        if len(q)==0 and count >0:
            return -1
            
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            new_i,new_j,t=q.pop()
            for temp_i,temp_j in d:
                cal_i=new_i + temp_i
                cal_j=new_j + temp_j
                if 0<= cal_i < r and 0<= cal_j <c and grid[cal_i][cal_j]==1:
                    grid[cal_i][cal_j]=2
                    q.appendleft((cal_i,cal_j,t+1))
                    count -= 1
                if len(q)==0 and count==0:
                    return t
                
        return -1
            