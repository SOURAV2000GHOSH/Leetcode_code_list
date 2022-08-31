class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        ans=[]
        cur=intervals[0]
        for nexti in intervals[1:]:
            if nexti[0]<=cur[1] and nexti[1]>cur[1]:
                cur=[cur[0],nexti[1]]
            if cur[0]<=nexti[0] and cur[1]>=nexti[1]:
                continue
            ans.append(cur)
            cur=nexti
        ans.append(cur)
        return ans
        
        
        