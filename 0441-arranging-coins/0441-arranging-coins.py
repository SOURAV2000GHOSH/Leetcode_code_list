class Solution:
    def arrangeCoins(self, n: int) -> int:
        stage_coin_num=1
        ans=0
        while n>0:
            n -= stage_coin_num
            if n<0:
                break
            ans+=1
            stage_coin_num += 1
        return ans
            
        