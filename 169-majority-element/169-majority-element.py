class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cheak=dict()
        major=nums[0]
        for indx,el in enumerate(nums):
            cheak[el]= 1 if el not in cheak else cheak[el]+1
            if cheak[el]>cheak[major]:
                major=el
        return major
                
        