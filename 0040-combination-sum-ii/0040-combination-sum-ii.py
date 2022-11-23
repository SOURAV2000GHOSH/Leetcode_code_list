class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def calculate(indx,n,target,arr,ans):
            if target==0:
                temp=[]
                for x in arr:
                    temp.append(x)
                ans.append(temp)
                return
            for i in range(indx,n):
                if i>indx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                arr.append(candidates[i])
                calculate(i+1,n,target-candidates[i],arr,ans)
                arr.pop()
        calculate(0,len(candidates),target,[],ans)
        return ans
        
        