class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        l,r=0,len(height)-1
        while l<r:
            temp=min(height[l],height[r])*(r-l)
            if temp>ans:
                ans=temp
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
                r-=1
        return ans
        