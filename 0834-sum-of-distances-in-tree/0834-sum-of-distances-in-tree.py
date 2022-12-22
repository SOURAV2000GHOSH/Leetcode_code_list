class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[0]*n
        g=[[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        q=[(0, 0)]
        parent=[None]*n
        s=0
        for v2 in g[0]:
            q.append((v2, 1))
            parent[v2]=0
        for curs in range(1, n):
            v, lev=q[curs]
            s+=lev
            lev+=1
            g[v].remove(parent[v])
            for v2 in g[v]:
                q.append((v2, lev))
                parent[v2]=v
        lst=[it[0] for it in q]
        chil_ct=[-2]*n
        for v in lst[n-1:0:-1]:
            chil_ct[parent[v]]+=chil_ct[v]
        ans[0]=s
        for v in lst:
            tmp=ans[v]+n
            par=parent[v]
            for v2 in g[v]:
                ans[v2]=tmp+chil_ct[v2]
        return ans
