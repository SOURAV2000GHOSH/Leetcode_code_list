class Solution:
    def swap(self,i,j,nums):
        nums[i],nums[j]=nums[j],nums[i]
    def traverse(self,ans,indx,n,nums):
        if indx==n:
            ans.append(nums[:])
            return
        for i in range(indx,n):
            self.swap(i,indx,nums)
            self.traverse(ans,indx+1,n,nums)
            self.swap(i,indx,nums)
                     
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        ans=[]
        self.traverse(ans,0,l,nums)
        return ans
        