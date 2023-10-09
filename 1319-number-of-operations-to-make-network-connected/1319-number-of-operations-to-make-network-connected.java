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
    
    public int makeConnected(int n, int[][] connections) {
        int l=connections.length;
        if(l<n-1){
            return -1;
        }
        int parent[]=new int[n];
        int rank[]=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        int component=n;
        for(int[] arr:connections){
            int parentX=Solution.findParent(arr[0],parent);
            int parentY=Solution.findParent(arr[1],parent);
            if(parentX!=parentY){
                Solution.union(arr[0],arr[1],parent,rank);
                component--;
            }
        }
        
        return component-1;
    }
}