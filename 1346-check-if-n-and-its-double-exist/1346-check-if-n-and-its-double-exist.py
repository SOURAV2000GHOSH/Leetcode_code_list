class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cheak=dict()
        for indx,el in enumerate(arr):
            cheak[el]=indx
        for indx,el in enumerate(arr):
            if el*2 in cheak and cheak[el*2] != indx:
                return True
        return False
        