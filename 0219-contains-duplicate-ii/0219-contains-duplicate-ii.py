class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cheak=dict()
        flag=False
        for i in range(len(nums)):
            if nums[i] not in cheak:
                cheak[nums[i]]=i
                continue
            if abs(i-cheak[nums[i]])<=k:
                flag=True
                break
            cheak[nums[i]]=i
        return flag
                