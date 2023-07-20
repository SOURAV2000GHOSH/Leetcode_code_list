class Solution:
    def traverse(self,temp,ans,n,check,nums):
        if len(temp)==n:
            ans.append(temp[:])
            return
        for j in range(n):
                if check[j]:
                    continue
                temp.append(nums[j])
                check[j]=True
                self.traverse(temp,ans,n,check,nums)
                temp.pop()
                check[j]=False
                # self.traverse(temp,ans,n,check,nums)              
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        ans=[]
        check=[False]*l
        self.traverse([],ans,l,check,nums)
        return ans
        