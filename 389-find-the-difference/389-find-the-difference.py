class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cheak=set(s)
        for x in t:
            if x not in cheak:
                return x
            if s.count(x)!=t.count(x):
                return x
        