import java.util.*;
class Solution {
    public static boolean solve(int u,int curCol,int []color,int [][]adj){
        color[u]=curCol;
        for(int v:adj[u]){
            if(color[v]==curCol){
                return false;
            }
            if(color[v]==-1 && !Solution.solve(v,1-curCol,color,adj)){
                return false;
            }
        }
        return true;
    }
    
    public boolean isBipartite(int[][] graph) {
        int V=graph.length;
        int []color=new int[V];
        Arrays.fill(color,-1);
        for(int i=0;i<V;i++){
            if(color[i]==-1 && !Solution.solve(i,0,color,graph)){
                return false;
            }
        }
        return true;
    }
}