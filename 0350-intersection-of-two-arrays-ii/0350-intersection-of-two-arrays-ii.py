class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp1=dict()
        temp2=dict()
        for x in nums1:
            temp1[x]=1 if x not in temp1 else temp1[x]+1
        for x in nums2:
            temp2[x]=1 if x not in temp2 else temp2[x]+1
        ans=[]
        for x in temp1.keys():
            if x in temp2:
                temp=min(temp1[x],temp2[x])
                for i in range(temp):
                    ans.append(x)
        return ans
        