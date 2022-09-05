class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        left_max=[0]*l
        for i in range(1,l):
            left_max[i]=max(left_max[i-1],height[i-1])
        right_max=[0]*l
        for i in range(l-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i+1])
        ans=0
        for x in range(l):
            level=min(left_max[x],right_max[x])
            if level>height[x]:
                ans += level-height[x]
        return ans