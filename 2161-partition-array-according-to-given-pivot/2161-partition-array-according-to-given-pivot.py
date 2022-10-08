class Solution(object):
    def pivotArray(self, nums, pivot):
        return [x for x in nums if x<pivot]+[x for x in nums if x==pivot]+[x for x in nums if x>pivot]
            
            
        
        