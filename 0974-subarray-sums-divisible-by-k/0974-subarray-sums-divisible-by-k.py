class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        Sum=0
        check=dict()
        check[0]=1
        for num in nums:
            Sum+=num
            rem=Sum%k
            if rem<0:
                rem+=k
            if rem in check:
                count += check[rem]
                check[rem] +=1
            else:
                check[rem]=1
        return count