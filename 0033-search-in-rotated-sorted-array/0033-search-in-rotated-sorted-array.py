class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for indx,el in enumerate(nums):
            if el==target:
                return indx
        return -1
        