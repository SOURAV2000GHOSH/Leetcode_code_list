# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=[-100000]
        def solve(root,maxSum):
            if not root:
                return 0
            l=solve(root.left,maxSum)
            r=solve(root.right,maxSum)
            niche_hi_mil_geya_ans = root.val+l+r
            koi_ek_achha_hai = max(l,r)+root.val
            only_root_achha_hai = root.val
            maxSum[0] = max(maxSum[0] , niche_hi_mil_geya_ans , koi_ek_achha_hai , only_root_achha_hai)
            return max(koi_ek_achha_hai , only_root_achha_hai)
        solve(root , maxSum)
        return maxSum[0]
        