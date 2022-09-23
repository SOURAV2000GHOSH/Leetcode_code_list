class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        lenth=0
        ans=0
        for x in range(1,n+1):
            if (x & (x-1))==0:
                lenth+=1
            ans=((ans<<lenth) | x) % mod
        return ans
                
        