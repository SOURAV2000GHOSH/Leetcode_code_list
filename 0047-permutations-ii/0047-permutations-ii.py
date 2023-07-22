class Solution:
    def swap(self,i,j,nums):
        nums[i],nums[j]=nums[j],nums[i]
    def dfs(self,nums,indx,n,ans,check):
        if indx==n:
            temp=tuple(nums)
            if temp not in check:
                ans.append(nums[:])
                check.add(temp)
            return
        for i in range(indx,n):
            if i>indx and nums[i]==nums[indx]:
                continue
            self.swap(i,indx,nums)
            self.dfs(nums,indx+1,n,ans,check)
            self.swap(i,indx,nums)
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        check=set()
        self.dfs(nums,0,len(nums),ans,check)
        return ans
        