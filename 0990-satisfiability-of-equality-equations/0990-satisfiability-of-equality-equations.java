class Solution {
    public static int findParent(int i,int []parent){
        if(parent[i]==i){
            return i;
        }
        parent[i]=Solution.findParent(parent[i],parent);
        return parent[i];
    }
    public static void union(int x,int y,int []parent,int []rank){
        int parentX=Solution.findParent(x,parent);
        int parentY=Solution.findParent(y,parent);
        if(parentX==parentY){
            return;
        }
        if(rank[parentY]==rank[parentX]){
            parent[parentY]=parentX;
            rank[parentX]++;
        }
        else if(rank[parentY]>rank[parentX]){
            parent[parentX]=parentY;
        }else{
            parent[parentY]=parentX;
        }
    }
    public boolean equationsPossible(String[] equations) {
        int []parent=new int[26];
        int []rank=new int[26];
        for(int i=0;i<26;i++){
            parent[i]=i;
        }
        for(String s:equations){
            if(s.charAt(1)=='='){
                int x=((int)s.charAt(0))-97;
                int y=((int)s.charAt(3))-97;
               Solution.union(x,y,parent,rank);
            }            
        }
        for(String s:equations){
            if(s.charAt(1)=='!'){
                int x=((int)s.charAt(0))-97;
                int y=((int)s.charAt(3))-97;
                int xParent=Solution.findParent(x,parent);
                int yParent=Solution.findParent(y,parent);
                if(xParent==yParent){
                    return false;
                }
            }
        }
        return true;
    }
}