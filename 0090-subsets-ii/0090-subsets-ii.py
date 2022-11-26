class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cheak=set()
        def calculate(indx,n,arr,ans,cheak):
            temp=tuple(arr)
            if indx>=n:
                if temp not in cheak:
                    a=[]
                    cheak.add(temp)
                    for x in arr:
                        a.append(x)
                    ans.append(a)
                return
            arr.append(nums[indx])
            calculate(indx+1,n,arr,ans,cheak)
            arr.pop()
            calculate(indx+1,n,arr,ans,cheak)
        nums.sort()
        calculate(0,len(nums),[],ans,cheak)
        return ans
        