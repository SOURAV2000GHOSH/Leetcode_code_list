class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=len(nums)//3
        ans=[]
        cheak1=set()
        cheak=dict()
        for indx,el in enumerate(nums):
            cheak[el]=1 if el not in cheak else cheak[el]+1
            if el not in cheak1 and cheak[el]>count:
                ans.append(el)
                cheak1.add(el)
        return ans