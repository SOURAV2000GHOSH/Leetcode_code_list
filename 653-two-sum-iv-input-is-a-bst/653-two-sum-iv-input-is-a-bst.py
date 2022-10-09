# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        temp=set()
        def inorder(root):
            if root:
                inorder(root.left)
                temp.add(root.val)
                inorder(root.right)
        inorder(root)
        while len(temp)>0:
            cheak=k-temp.pop()
            if cheak in temp:
                return True
        return False
        