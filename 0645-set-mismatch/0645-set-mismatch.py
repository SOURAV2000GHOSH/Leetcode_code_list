class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ap=l*(l+1)//2
        s=sum(set(nums))
        missing_number = ap-s
        dupplicate_number = sum(nums)-ap+missing_number
        
        return [dupplicate_number,missing_number]