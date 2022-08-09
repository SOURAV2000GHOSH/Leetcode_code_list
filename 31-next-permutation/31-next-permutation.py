class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l <= 2:
            return nums.reverse()
        pointer = l - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer +1]:
            pointer -= 1
        if pointer == -1:
            return nums.reverse()
        for x in range(l-1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer],nums[x]=nums[x],nums[pointer]
                break
        nums[pointer + 1 :] = reversed(nums[pointer + 1 :])
        
                