class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left=nums[:mid]
                right=nums[mid:]
                mergesort(left)
                mergesort(right)
                lp=rp=np=0
                while rp<len(right) and lp<len(left):
                    if left[lp]<right[rp]:
                        nums[np]=left[lp]
                        lp+=1
                    elif left[lp]>right[rp]:
                        nums[np]=right[rp]
                        rp+=1
                    else:
                        nums[np]=left[lp]
                        lp+=1
                    np+=1
                while lp<len(left):
                    nums[np]=left[lp]
                    lp+=1
                    np+=1
                while rp<len(right):
                    nums[np]=right[rp]
                    np+=1
                    rp+=1
            return nums
        return mergesort(nums)
        