class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l=0
        r=len(num)-1
        while l<r:
            temp=num[l]+num[r]
            if temp>target:
                r -= 1
            elif temp< target:
                l += 1
            else:
                return [l+1,r+1]
        return []
            
        