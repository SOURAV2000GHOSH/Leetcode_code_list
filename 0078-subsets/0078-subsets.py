class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def subsequence(indx,arr,n):
            if indx >= n:
                temp=[]
                for x in arr:
                    temp.append(x)
                ans.append(temp)
                return
            arr.append(nums[indx])
            #not taking number
            subsequence(indx+1,arr,n)
            arr.pop(-1)
            subsequence(indx+1,arr,n)
        temp=[]
        subsequence(0,temp,len(nums))
        return ans
        