class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count=[0]*n
        for x,y in trust:
            x-=1
            y-=1
            count[x]-=1
            count[y]+=1
        val=-2
        for i in range(n):
            if count[i]==(n-1):
                val=i
                break
        return val+1
                
        