class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(nums,arr,index,n,ans):
            if len(arr)>1:
                temp=[]
                for el in arr:
                    temp.append(el)
                ans.append(temp)
            check=set()
            for i in range(index,n):
                if (len(arr)==0 or arr[-1]<=nums[i]) and nums[i] not in check:
                    arr.append(nums[i])
                    solve(nums,arr,i+1,n,ans)
                    arr.pop()
                    check.add(nums[i])
            
        solve(nums,[],0,len(nums),ans)
        return ans
            