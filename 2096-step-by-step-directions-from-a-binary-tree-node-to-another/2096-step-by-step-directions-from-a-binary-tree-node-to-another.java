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
class Node{
    int level;
    TreeNode root;
    public Node(int l,TreeNode r){
        level=l;
        root=r;
    }
}
class Solution {
    Map<Integer,Node> startParents;
    Map<Integer,Node> destParents;
    public boolean findParent(TreeNode root,int value,int level,Map<Integer,Node> store){
        if(root==null)
            return false;
        if(root.val==value){
            store.put(value,new Node(level,root));
            return true;
        }
        if(findParent(root.left,value,level+1,store) || findParent(root.right,value,level+1,store)){
            store.put(root.val,new Node(level,root));
            return true;
        }
        return false;
    }
    
    public String pathFind(TreeNode root,int val,StringBuilder sb) {
        if(root==null)
            return "";
        if(root.val==val){
            System.out.println(sb.toString());
            return sb.toString();
        }
        sb.append("L");
        String left = pathFind(root.left,val,sb);
        sb.deleteCharAt(sb.length()-1);
        sb.append("R");
        String right = pathFind(root.right,val,sb);
        sb.deleteCharAt(sb.length()-1);
        return left.length()>right.length() ? left : right;
        
    }
    public String getDirections(TreeNode root, int startValue, int destValue) {
        //finding all ancestor
        startParents=new HashMap<>();
        destParents=new HashMap<>();
        findParent(root,startValue,0,startParents);
        findParent(root,destValue,0,destParents);
        // getting common closest ancestor
        TreeNode commonParent=null;
        int parentLavel=-1;
        for(int x: destParents.keySet()){
            if(startParents.containsKey(x) && startParents.get(x).level>parentLavel){
                commonParent=startParents.get(x).root;
                parentLavel=startParents.get(x).level;
            }
        }
        StringBuilder ans=new StringBuilder();
        if(destValue == commonParent.val){
            TreeNode temp=commonParent;
            StringBuilder str = new StringBuilder();
            String string = pathFind(temp,startValue,str);
            for(int i=0;i<string.length();i++){
                ans.append("U");
            }
            return ans.toString();
        }else if(startValue == commonParent.val){
            TreeNode temp=commonParent;
            StringBuilder str = new StringBuilder();
            String string = pathFind(temp,destValue,str);
            return string;
        }else{
            TreeNode temp=commonParent;
            StringBuilder str = new StringBuilder();
            String string = pathFind(temp,startValue,str);
            for(int i=0;i<string.length();i++){
                ans.append("U");
            }
            temp=commonParent;
            str = new StringBuilder();
            string = pathFind(temp,destValue,str);
            return ans.toString()+string;
        }
        
    }
}