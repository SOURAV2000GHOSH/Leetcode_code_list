class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph=dict()
        l1=len(s1)
        for i in range(l1):
            if s1[i] in graph:
                graph[s1[i]].append(s2[i])
            else:
                graph[s1[i]]=[s2[i]]
            if s2[i] in graph:
                graph[s2[i]].append(s1[i])
            else:
                graph[s2[i]]=[s1[i]]
                
        ans=["1"]*len(baseStr)
        def getMinChar(graph,visited,character):
            if character not in graph:
                return character
            minChar=character
            visited.add(minChar)
            for cur in graph[character]:
                if cur in visited:
                    continue
                tempChar=getMinChar(graph,visited,cur)
                if ord(minChar)>ord(tempChar):
                    minChar=tempChar
            return minChar
        for i in range(len(baseStr)):
            visited=set()
            minChar=getMinChar(graph,visited,baseStr[i])
            ans[i]=minChar
        return "".join(ans)
        