class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
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
        def check(graph,visited,s,d):
            if s==d:
                return True
            if s in visited:
                return False
            visited.add(s)
            for node in graph[s]:
                if check(graph,visited,node,d):
                    return True
            return False
        return check(graph,visited,source,destination)