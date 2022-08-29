# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=collections.deque()
        ans=[]
        q.append((root))
        while q:
            l=len(q)
            for i in range(l):
                el=q.popleft()
                if i==0:
                    ans.append(el.val)
                if el.right:
                    q.append(el.right)
                if el.left:
                    q.append(el.left)
        return ans
        
        