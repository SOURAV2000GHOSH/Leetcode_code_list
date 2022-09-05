class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        val=0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                val+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                val+=rmax-height[r]
                
        return val
            