class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binarySearch(arr,num,size):
            l=0
            r=size-1
            result=-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=num:
                    result=mid
                    l=mid+1
                else:
                    r=mid-1
            return result+1
        nums.sort()
        ans=[0]*len(queries)
        cumilative=[]
        total=0
        for i in nums:
            total+=i
            cumilative.append(total)
        l=0
        length=len(cumilative)
        for j in queries:
            ans[l]=binarySearch(cumilative,j,length)
            l+=1
        return ans
        