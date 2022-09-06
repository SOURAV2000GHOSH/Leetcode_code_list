class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        set_col=image[sr][sc]
        r,c=len(image),len(image[0])
        st=[(sr,sc)]
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        while len(st)>0:
            temr,temc=st.pop(-1)
            image[temr][temc]=color
            for dr,dc in direction:
                calr=temr+dr
                calc=temc+dc
                if 0<=calr<r and 0<=calc<c and image[calr][calc]==set_col:
                    st.append((calr,calc))
        return image
        