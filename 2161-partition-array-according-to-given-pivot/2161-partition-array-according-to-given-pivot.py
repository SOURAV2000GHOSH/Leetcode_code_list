class Solution(object):
    def pivotArray(self, nums, pivot):
        temp=[]
        for x in nums:
            temp.append(x)
        l=len(temp)
        i=0
        for x in temp:
            if x<pivot:
                nums[i]=x
                i+=1
        for x in temp:
            if x==pivot:
                nums[i]=x
                i+=1
        for x in temp:
            if x>pivot:
                nums[i]=x
                i+=1
        return nums
            
            
        
        