class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        l=len(rocks)
        dif=[0]*l
        for i in range(l):
            dif[i]=capacity[i]-rocks[i]
        dif.sort()
        count=0
        for i in range(l):
            if additionalRocks<dif[i]:
                break
            count+=1
            additionalRocks-=dif[i]
        return count