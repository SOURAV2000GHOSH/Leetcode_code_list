# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l,r=self.dll(root)
        while l.val != r.val:
            temp=l.val+r.val
            if temp >k:
                r=r.left
            elif temp < k:
                l=l.right
            else:
                return True
        return False
    def dll(self,root):
        if not root:
            return None,None
        lh,lt=self.dll(root.left)
        rh,rt=self.dll(root.right)
        if lh:
            l=lh
            lt.right=root
            root.left=lt
        else:
            l=root
        if rh:
            r=rt
            root.right=rh
            rh.left=root
        else:
            r=root
        return l,r
        
        