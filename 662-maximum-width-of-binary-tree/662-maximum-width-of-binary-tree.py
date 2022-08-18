# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=[(root,0)]
        width =1
        while q:
            if len(q)>1:
                width=max(width,q[-1][1]-q[0][1]+1)
            l=len(q)
            for x in range(l):
                el,temp_width=q.pop(0)
                if el.left:
                    q.append((el.left,2*temp_width))
                if el.right:
                    q.append((el.right,2*temp_width+1))
                    
        return width
        