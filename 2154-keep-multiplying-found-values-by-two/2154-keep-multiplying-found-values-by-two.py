class Solution(object):
    def findFinalValue(self, nums, original):
        cheak=set(nums)
        while original in cheak:
            original *= 2
        return original