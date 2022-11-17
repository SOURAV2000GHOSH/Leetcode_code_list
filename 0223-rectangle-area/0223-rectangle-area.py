
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #area of rectangle 1
        ax=(ax2-ax1)
        ay=(ay2-ay1)
        area1=ax*ay
        #area of rectangle 2
        bx=(bx2-bx1)
        by=(by2-by1)
        area2=bx*by
        #area of common rectangle
        extra_area=0
        cx1=max(ax1,bx1)
        cy1=max(ay1,by1)
        cx2=min(ax2,bx2)
        cy2=min(ay2,by2)
        cx=cx2-cx1
        cy=cy2-cy1
        if cx>0 and cy>0:
            extra_area=cx*cy
        return area1+area2-extra_area