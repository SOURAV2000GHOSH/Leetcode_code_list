class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #dfs
        def dfs(graph,visited,s,d):
            if s==d:
                return True
            if s in visited:
                return False
            visited.add(s)
            for node in graph[s]:
                if dfs(graph,visited,node,d):
                    return True
            return False
        
        graph=dict()
        for x,y in edges:
            if x not in graph:
                graph[x]=[y]
            else:
                graph[x].append(y)
            if y not in graph:
                graph[y]=[x]
            else:
                graph[y].append(x)
        visited=set()
        #return check(graph,visited,source,destination)
        #bfs
        q=deque()
        q.appendleft(source)
        while q:
            el=q.pop()
            if el==destination:
                return True
            if el in visited:
                continue
            visited.add(el)
            for node in graph[el]:
                q.appendleft(node)
        return False