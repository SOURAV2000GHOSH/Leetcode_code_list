class Solution:
    def dfs(self,temp,store,ans,n):
        if len(temp)==n:
            ans.append(temp[:])
            return
        for i in store:
            if store[i]>0:
                temp.append(i)
                store[i]-=1
                self.dfs(temp,store,ans,n)
                temp.pop()
                store[i]+=1
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        store=dict()
        for i in nums:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
        ans=[]
        self.dfs([],store,ans,len(nums))
        return ans
        