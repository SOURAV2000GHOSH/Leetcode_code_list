class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def traverse(graph,s,d,ans,temp,node):
            temp.append(node)
            if node==d:
                use=[]
                for el in temp:
                    use.append(el)
                ans.append(use)
            for j in graph[node]:
                traverse(graph,s,d,ans,temp,j)
                temp.pop()
        ans=[]
        temp=[]
        s=0
        d=len(graph)-1
        traverse(graph,s,d,ans,temp,0)
        return ans
        
        