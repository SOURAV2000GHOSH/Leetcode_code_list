"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        def post(root):
            if root:
                for x in root.children:
                    post(x)
                    ans.append(x.val)
        post(root)
        if root:
            ans.append(root.val)
        return ans
                
        