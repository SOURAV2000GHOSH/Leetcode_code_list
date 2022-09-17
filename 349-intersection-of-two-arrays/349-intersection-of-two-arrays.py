class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        temp={}
        for x in nums1:
            temp[x]=temp[x]+1 if x in temp else 1
        for y in nums2:
            if y in temp and temp[y]>0:
                ans.append(y)
                temp[y]=0
        return ans
        