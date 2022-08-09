class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,el in enumerate(nums):
            if (target-el) in nums and  nums.index(target-el) != i:
                return [i,nums.index(target-el)]
        