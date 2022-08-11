# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        iseven=True
        ans=[]
        q.appendleft(root)
        while q:
            tem=[]
            l=len(q)
            if iseven:
                for i in range(l):
                    ele=q.pop()
                    tem.append(ele.val)
                    if ele.left:
                        q.appendleft(ele.left)
                    if ele.right:
                        q.appendleft(ele.right)
                ans.append(tem)
            else:
                for i in range(l):
                    ele=q.popleft()
                    tem.append(ele.val)
                    if ele.right:
                        q.append(ele.right)
                    if ele.left:
                        q.append(ele.left)
                ans.append(tem)
            iseven = not iseven
        
        return ans
                
                        
                        
                
        