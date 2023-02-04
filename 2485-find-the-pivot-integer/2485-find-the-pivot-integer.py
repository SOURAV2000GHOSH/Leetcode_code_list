class Solution:
    def pivotInteger(self, n: int) -> int:
        total=(n*(n+1))/2
        a=0
        for i in range(1,(n+1)):
            a+=i
            if a==((total-a)+i):
                return i
        return -1
        