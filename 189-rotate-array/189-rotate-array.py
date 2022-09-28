class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(k):
            l=nums.pop()
            nums.insert(0,l)
        