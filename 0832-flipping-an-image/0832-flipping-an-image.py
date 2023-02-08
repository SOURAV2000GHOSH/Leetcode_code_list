class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        for i in range(n):
            l=0
            r=n-1
            while l<r:
                image[i][l],image[i][r]=image[i][r],image[i][l]
                l+=1
                r-=1
        for i in range(n):
            for j in range(n):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image
        