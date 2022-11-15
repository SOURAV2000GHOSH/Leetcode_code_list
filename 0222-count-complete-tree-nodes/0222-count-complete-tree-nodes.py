# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q=deque()
        count=0
        if not root:
            return count
        q=deque()
        q.appendleft(root)
        while q:
            count+=1
            el=q.pop()
            if el.left:
                q.appendleft(el.left)
            if el.right:
                q.appendleft(el.right)
        return count
        