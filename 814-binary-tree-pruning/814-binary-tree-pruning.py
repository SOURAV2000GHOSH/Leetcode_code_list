# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getans(root):
            if not root:
                return False
            left_contain_one=getans(root.left)
            right_contain_one=getans(root.right)
            if not left_contain_one:
                root.left=None
            if not right_contain_one:
                root.right=None
            return root.val or right_contain_one or left_contain_one
        
        
        return root if getans(root) else None