# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            l=len(q)
            add=0
            for i in range(l):
                el=q.popleft()
                add += el.val
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ans.append(add/l)
        return ans
        