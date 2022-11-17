class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #common area rectangle left-buttom point
        x1=max(rec1[0],rec2[0])
        y1=max(rec1[1],rec2[1])
        
        #common area rectangle right-top point
        x2=min(rec1[2],rec2[2])
        y2=min(rec1[3],rec2[3])
        
        #common area rectangle length & width
        x=x2-x1
        y=y2-y1
        
        #cheaking have common area
        if x>0 and y>0:
            return True
        return False
        