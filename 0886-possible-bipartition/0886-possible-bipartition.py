class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfsCheak(adj_list,node,color):
            q=deque()
            q.append(node)
            color[node]=1
            while q:
                u=q.popleft()
                for v in adj_list[u]:
                    if color[v]==color[u]:
                        return False
                    if color[v]==-1:
                        color[v]=1-color[u]
                        q.append(v)
            return True
        
        adj_list=dict()
        color=[-1]*(n+1)
        for x,y in dislikes:
            if x in adj_list:
                adj_list[x].append(y)
            else:
                adj_list[x]=[y]
            if y in adj_list:
                adj_list[y].append(x)
            else:
                adj_list[y]=[x]
        q=deque()
        for i in range(1,n):
            if color[i]==-1 and i in adj_list:
                if not bfsCheak(adj_list,i,color):
                    return False
        return True
                        
        