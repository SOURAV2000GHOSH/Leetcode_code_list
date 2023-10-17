class Solution {
    static int nodeCount=0;
    public static int find(int i,int []parent){
        if(parent[i]==i){
            return i;
        }
        parent[i]=Solution.find(parent[i],parent);
        return parent[i];
    }
    public static boolean union(int c,int p,int []parent){
        int parentC=Solution.find(c,parent);
        int parentP=Solution.find(p,parent);
        if(parentC!=c){
            return false;
        }
        if(parentP==c){
            return false;
        }
        parent[c]=p;
        Solution.nodeCount--;
        return true;
    }
    
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        Solution.nodeCount=n;
        int parent[]=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        for(int i=0;i<n;i++){
            int l=leftChild[i];
            int r=rightChild[i];
            if(l!=-1 && !Solution.union(l,i,parent)){
                return false;
            }
            if(r!=-1 && !Solution.union(r,i,parent)){
                return false;
            }
        }
        return Solution.nodeCount==1;
        
    }
}