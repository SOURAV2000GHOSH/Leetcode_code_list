# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def calculate(root,arr):
            if not root.left and not root.right:
                arr.append(root.val)
                return
            if root.left:
                calculate(root.left,arr)
            if root.right:
                calculate(root.right,arr)
        ans1=[]
        ans2=[]
        calculate(root1,ans1)
        calculate(root2,ans2)
        l1=len(ans1)
        l2=len(ans2)
        if l1!=l2:
            return False
        for i in range(l1):
            if ans1[i]!=ans2[i]:
                return False
        return True
            

        