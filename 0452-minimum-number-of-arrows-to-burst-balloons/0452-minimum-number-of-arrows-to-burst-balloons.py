class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        points.sort()
        arrow=1
        prevStart=points[0][0]
        prevEnd=points[0][1]
        for i in range(1,n):
            curStart=points[i][0]
            curEnd=points[i][1]
            if curStart>prevEnd:
                arrow+=1
                prevStart=curStart
                prevEnd=curEnd
            else:
                prevStart=max(prevStart,curStart)
                prevEnd=min(prevEnd,curEnd)
        return arrow