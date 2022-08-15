# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
prev=None
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global prev
        prev=-(2**31+1)
        return  self.fun(root)
    def fun(self,root):
        if root:
            if not self.fun(root.left):
                return False
            global prev
            if prev >= root.val:
                return False
            prev=root.val
            return self.fun(root.right)
            
        return True