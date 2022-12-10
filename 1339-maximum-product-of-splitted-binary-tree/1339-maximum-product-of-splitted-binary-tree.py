# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def CalculateTotal(root):
            if not root:
                return 0
            return root.val+CalculateTotal(root.left)+CalculateTotal(root.right)
        total=CalculateTotal(root)
        maxMulti=[0]
        def calculate(root,maxMulti):
            if not root:
                return 0;
            l=calculate(root.left,maxMulti)
            r=calculate(root.right,maxMulti)
            subSum=root.val+l+r
            temp=total-subSum
            tempMulti=temp*subSum
            maxMulti[0]=max(maxMulti[0],tempMulti)
            return subSum
            
        calculate(root,maxMulti)
            
        return maxMulti[0]%(1000000007)
            
            