class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for i in xrange(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif s > target:
                    r -= 1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                else: 
                    return res
        return res