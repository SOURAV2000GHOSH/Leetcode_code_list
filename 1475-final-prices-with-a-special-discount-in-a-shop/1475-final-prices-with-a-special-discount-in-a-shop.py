class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l=len(prices)
        ans=[0]*l
        for x in range(l):
            for y in range(x+1,l):
                if prices[x]>=prices[y]:
                    ans[x]=prices[x]-prices[y]
                    break
                else:
                    ans[x]=prices[x]
        ans[l-1]=prices[l-1]
        
        return ans