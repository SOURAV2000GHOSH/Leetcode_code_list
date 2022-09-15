class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []
        ans=[]
        q=collections.deque()
        changed.sort()
        for x in changed:
            if len(q)>0 and q[0]==x:
                q.popleft()
            else:
                q.append(2*x)
                ans.append(x)
        if len(q)>0:
            return []
        return ans
            
                