class Solution:
    def countOdds(self, l: int, h: int) -> int:
        if l%2==0 and h%2==0:
            return (h-l)//2
        if (l%2==0 and h%2==1) or (l%2==1 and h%2==0):
            return ((h-l)//2)+1
        if l%2==1 and h%2==1:
            return ((h-l)//2)+1