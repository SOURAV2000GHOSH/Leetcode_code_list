class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=dict()
        for x,y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x]=[y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y]=[x]
                
        def dfs(graph,node,par,hasApple):
            time=0
            for cur in graph[node]:
                if cur==par:
                    continue
                time_from_child=dfs(graph,cur,node,hasApple)
                if time_from_child>0 or hasApple[cur]==True:
                    time+=(time_from_child+2)
            return time
        return dfs(graph,0,-1,hasApple)
            
        
        