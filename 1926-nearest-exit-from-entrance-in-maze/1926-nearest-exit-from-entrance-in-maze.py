class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m=len(maze)-1
        n=len(maze[0])-1
        q=deque()
        q.append(tuple(entrance))
        visited=set()
        visited.add(tuple(entrance))
        level=0
        while len(q)>0:
            l=len(q)
            
            for i in range(l):
                position_x,position_y=q.popleft()
                if [position_x,position_y] != entrance and (position_x==0 or position_x==m or position_y==0 or position_y==n):
                    return level
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    cur_i=position_x+x
                    cur_j=position_y+y
                    if 0<=cur_i<=m and 0<=cur_j<=n and maze[cur_i][cur_j]=="." and (cur_i,cur_j) not in visited:
                        q.append((cur_i,cur_j))
                        visited.add((cur_i,cur_j))
            level+=1
        return -1
                
            
            