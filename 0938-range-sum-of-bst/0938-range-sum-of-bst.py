# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        q=deque()
        q.append(root)
        while q:
            el=q.popleft()
            if low<=el.val<=high:
                ans+=el.val
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)
        return ans