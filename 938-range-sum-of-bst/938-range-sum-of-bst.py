# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q=deque()
        q.appendleft(root)
        ans=0
        while q:
            ele=q.pop()
            if low <= ele.val <= high:
                ans += ele.val
            if ele.left:
                q.appendleft(ele.left)
            if ele.right:
                q.appendleft(ele.right)
        return ans