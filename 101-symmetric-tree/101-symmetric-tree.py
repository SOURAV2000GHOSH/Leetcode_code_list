# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.symmetric(root.left,root.right)
    
    
    def symmetric(self,p,q):
        if p and q:
            return 1 if (p.val==q.val) and self.symmetric(p.left,q.right) and self.symmetric(p.right,q.left) else 0
        return 1 if p == q else 0