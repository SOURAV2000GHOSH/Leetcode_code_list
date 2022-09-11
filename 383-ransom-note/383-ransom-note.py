class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        if len(r)>len(m):
            return False
        a=set(r)
        for x in a:
            if r.count(x) > m.count(x):
                return False
        return True
        