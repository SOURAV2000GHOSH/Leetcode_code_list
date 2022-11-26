class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def calculate(indx,n,arr,ans):
            ans.append([x for x in arr])
            for i in range(indx,n):
                if i>indx and nums[i]==nums[i-1]:
                    continue
                arr.append(nums[i])
                calculate(i+1,n,arr,ans)
                arr.pop()
        nums.sort()
        calculate(0,len(nums),[],ans)
        return ans
        