class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        #this function calculate and and append list in ans
        def calculate(indx,n,arr,total,target):
            #if indx 
            if indx==n:
                return
            if total==target:
                temp=[]
                for x in arr:
                    temp.append(x)
                ans.append(temp)
                return
            elif total>target:
                return
            arr.append(candidates[indx])
            total+=candidates[indx]
            calculate(indx,n,arr,total,target)
            arr.pop()
            total-=candidates[indx]
            calculate(indx+1,n,arr,total,target)
        calculate(0,len(candidates),[],0,target)

        return ans