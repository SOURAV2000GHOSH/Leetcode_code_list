class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=[]
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                if len(ans)>0:
                    ans.pop()
                ans.append(mid)
                r=mid-1
            elif nums[mid]<target:
                l= mid+1
            else:
                r=mid-1
        r=None
        if len(ans)>0:
            r=ans[0]
        while len(ans)>0 and r>-1 and r<len(nums)-1 and nums[r+1]==target:
            r+=1
            ans.append(r)
        return ans
            
        