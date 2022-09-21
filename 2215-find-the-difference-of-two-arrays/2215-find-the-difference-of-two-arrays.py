class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[[],[]]
        temp1=set(nums1)
        temp2=set(nums2)
        for x in temp1:
            if x not in temp2:
                ans[0].append(x)
                continue
            temp2.remove(x)
        for x in temp2:
            ans[1].append(x)
        return ans
        