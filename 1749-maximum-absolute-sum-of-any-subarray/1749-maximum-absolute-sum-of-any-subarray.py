class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_pos_sum=0
        cur_neg_sum=0
        maxsum=0
        for x in nums:
            cur_pos_sum += x
            cur_neg_sum += x
            if cur_pos_sum <0:
                cur_pos_sum=0
            if cur_neg_sum>0:
                cur_neg_sum=0
            maxsum=max(maxsum,abs(cur_pos_sum),abs(cur_neg_sum))
                
        return maxsum