# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def solve(root):
            if root:
                solve(root.left)
                ans.append(root.val)
                solve(root.right)
        solve(root)
        l=len(ans)
        dif=ans[1]-ans[0]
        for i in range(1,len(ans)):
            dif=min(dif,(ans[i]-ans[i-1]))
        return dif
        