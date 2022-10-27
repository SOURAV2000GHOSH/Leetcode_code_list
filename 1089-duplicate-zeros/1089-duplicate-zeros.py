class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count=0
        l=0
        n=len(arr)
        while l<n:
            if arr[l]==0 and l<n-1:
                arr.insert(l+1,0)
                arr.pop()
                l+=2
            else:
                l+=1
        
                
        