brute force
```
class Solution:
def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
nums.sort()
ans=[0]*len(queries)
l=0
for i in queries:
count=0
for j in nums:
i-=j
if i<0:
break
count+=1
ans[l]=count
l+=1
return ans
```