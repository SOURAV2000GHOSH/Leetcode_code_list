/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void traverse(TreeNode root,int []arr){
        if(root.left==null && root.right==null){
            arr[0]+=root.val;
            root.val=arr[0];
            return;
        }
        if(root.right!=null){
            traverse(root.right,arr);
        }
        arr[0]+=root.val;
        root.val=arr[0];
        if(root.left!=null){
            traverse(root.left,arr);
        }
    }
    public TreeNode convertBST(TreeNode root) {
        if(root==null){
            return root;
        }
        int []arr={0};
        traverse(root,arr);
        return root;
    }
}