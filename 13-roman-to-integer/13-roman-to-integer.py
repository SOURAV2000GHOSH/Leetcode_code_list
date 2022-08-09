class Solution:
    def romanToInt(self, s: str) -> int:
        a={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0
        l=[]
        for x in s:
            l.append(x)
        x=0
        while x<len(l):
            if x<len(l)-1 and a[l[x]]<a[l[x+1]]:
                sum += (a[l[x+1]] - a[l[x]])
                x += 2
            else:
                sum += a[l[x]]
                x += 1
        return sum