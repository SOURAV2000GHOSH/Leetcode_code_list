class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eleSum=0
        digSum=0
        for i in nums:
            eleSum += i
            for j in str(i):
                digSum+=int(j)
        return abs(eleSum-digSum)