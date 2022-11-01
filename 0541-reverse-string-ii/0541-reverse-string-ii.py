class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp=list(s)
        start=0
        end=k-1
        if k>=len(s):
            start=0
            end=len(s)-1
            while start<end:
                temp[start],temp[end]=temp[end],temp[start]
                start+=1
                end-=1
            return "".join(temp)
            
        while start<len(s):
            temp_position=[start,end]
            while start<end:
                temp[start],temp[end]=temp[end],temp[start]
                start+=1
                end-=1
            start=temp_position[0]+(2*k)
            end=min(temp_position[1]+(2*k),len(s)-1)
        return "".join(temp)
        