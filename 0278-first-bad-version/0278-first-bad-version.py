# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s=1
        e=n
        while s<e:
            mid = s+(e-s)//2
            if isBadVersion(mid):
                e=mid
            else:
                s=mid+1
        # if isBadVersion(s):
        return s
       
        