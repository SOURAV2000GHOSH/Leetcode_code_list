class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for x in range(len(nums)):
            indx=index[x]
            value=nums[x]
            #cheaking the given index is greater or not if geater then value will be append.
            if indx>len(target):
                target.append(value)
            else:
                target.insert(indx,value)
        return target