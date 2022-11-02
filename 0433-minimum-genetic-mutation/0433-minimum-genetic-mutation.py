class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        check=set(bank)
        if end not in bank:
            return -1
        q=deque()
        q.appendleft((start,0))
        visited=set()
        while len(q)>0:
            gene,level=q.pop()
            if gene==end:
                return level
            for i in range(len(gene)):
                for letter in 'ACGT':
                    new_gene=gene[:i]+letter+gene[i+1:]
                    if new_gene not in visited and new_gene in check:
                        q.appendleft((new_gene,level+1))
                        visited.add(new_gene)
        
        return -1
            
        