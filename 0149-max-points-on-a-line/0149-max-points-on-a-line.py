class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)==1):
            return 1
        result=0
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dy=(points[j][1]-points[i][1])
                dx=(points[j][0]-points[i][0])
                count=2
                for k in range(len(points)):
                    if(k!=i and k!=j):
                        dy_=(points[k][1]-points[i][1])
                        dx_=(points[k][0]-points[i][0])
                        if((dy*dx_)==(dy_*dx)):
                            count += 1
                result=max(result,count)
        return result