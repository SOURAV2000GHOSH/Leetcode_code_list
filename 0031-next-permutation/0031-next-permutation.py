class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if l==1:
            return
        if l==2:
            nums.reverse()
            return
        small=l-2
        while small>=0 and nums[small]>=nums[small+1]:
            small-=1
        if small==-1:
            nums.reverse()
            return
        big=l-1
        while nums[big]<=nums[small]:
            big-=1
        nums[small],nums[big]=nums[big],nums[small]
        small+=1
        big=l-1
        while small<big:
            nums[small],nums[big]=nums[big],nums[small]
            small+=1
            big-=1
        