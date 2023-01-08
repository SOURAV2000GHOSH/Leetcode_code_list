class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points)==1):
            return 1
        result=0
        for i in range(len(points)):
            check=dict()
            for j in range(len(points)):
                if j==i:
                    continue
                dy=(points[j][1]-points[i][1])
                dx=(points[j][0]-points[i][0])
                thita = math.atan2(dy,dx)
                if thita in check:
                    check[thita]+=1
                else:
                    check[thita]=1
                result=max(result,check[thita])
            # for value in check.values():
            #     result=max(result,value)
        return result+1