class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        check=set(jewels)
        for i in stones:
            if i in check:
                count+=1
        return count
        