class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        temp1=set(nums1)
        temp2=set(nums2)
        for x in temp1:
            if x in temp2:
                ans.append(x)
        return ans
        