class Solution:
    def removeElement(self, n: List[int], val: int) -> int:
        if len(n)==1 and n[0]==val:
            return 0
        index=0
        for i in range(len(n)):
            if n[i] != val:
                n[index]=n[i]
                index += 1
        return index
        
