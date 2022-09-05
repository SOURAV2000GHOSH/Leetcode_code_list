"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def pre(root):
            if root:
                for x in root.children:
                    ans.append(x.val)
                    pre(x)
        if root:
            ans.append(root.val)
        pre(root)
        return ans
                    
        