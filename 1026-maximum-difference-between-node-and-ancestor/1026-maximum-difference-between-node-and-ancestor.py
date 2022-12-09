# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def calculate(root,minNum,maxNum):
            if not root:
                return maxNum-minNum
            minNum=min(minNum,root.val)
            maxNum=max(maxNum,root.val)
            l=calculate(root.left,minNum,maxNum)
            r=calculate(root.right,minNum,maxNum)
            return max(l,r)
        return calculate(root,1000000,0)