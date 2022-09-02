# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=deque([root])
        while q:
            temp=[]
            l=len(q)
            for i in range(l):
                el=q.popleft()
                temp.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ans.append(temp)
        x=[]
        for i in range(len(ans)):
            x.append(ans.pop())
        return x
        
        