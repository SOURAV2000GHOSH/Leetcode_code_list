class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cheak1=set()
        cheak2=set()
        ans=0
        for x in nums:
            if x not in cheak1:
                if x not in cheak2:
                    ans += x
                    cheak1.add(x)
                else:
                    continue
            else:
                ans -= x
                cheak2.add(x)
                cheak1.remove(x)
        
        return ans
        