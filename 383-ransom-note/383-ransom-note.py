class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        a=set(r)
        for x in a:
            if r.count(x) > m.count(x):
                return False
        return True
        