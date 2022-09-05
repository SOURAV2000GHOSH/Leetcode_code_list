"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=deque([root])
        while q:
            temp=[]
            l=len(q)
            for i in range(l):
                el=q.popleft()
                temp.append(el.val)
                for i in el.children:
                    q.append(i)
                
            ans.append(temp)
        return ans