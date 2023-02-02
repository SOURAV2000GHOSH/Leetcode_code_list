class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        check=dict()
        for i in range(len(order)):
            check[order[i]]=i
        for i in range(len(words)-1):
            cur=words[i]
            nex=words[i+1]
            l=min(len(cur),len(nex))
            if l != len(cur) and l == len(nex) and cur.startswith(nex):
                return False
            for i in range(l):
                if check[cur[i]]>check[nex[i]]:
                    return False
                if check[cur[i]]<check[nex[i]]:
                    break
        return True
        