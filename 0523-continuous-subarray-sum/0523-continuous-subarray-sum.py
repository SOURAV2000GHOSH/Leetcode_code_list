class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cheak={0:-1}
        total=0
        for indx,el in enumerate(nums):
            total += el
            rem = total %k
            if rem not in cheak:
                cheak[rem]=indx
            elif indx-cheak[rem]>1:
                return True
        return False
        