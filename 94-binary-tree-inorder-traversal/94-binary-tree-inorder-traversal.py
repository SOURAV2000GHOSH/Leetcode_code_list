# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lin=[]
        self.inorder(root,lin)
        return lin
        
    def inorder(self,root,l):
        if not root:
            return
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
        