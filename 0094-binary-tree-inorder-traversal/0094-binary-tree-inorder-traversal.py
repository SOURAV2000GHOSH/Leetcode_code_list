# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder=[]
        arr=[]
        node=root
        while True:
            if node:
                arr.append(node)
                node=node.left
            else:
                if len(arr)==0:
                    break
                node=arr.pop()
                inorder.append(node.val)
                node=node.right
        return inorder
                
                
                