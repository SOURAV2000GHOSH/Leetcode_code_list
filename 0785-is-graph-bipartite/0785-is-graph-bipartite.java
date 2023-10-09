import java.util.*;
class Node{
    int vertex;
    int color;
    public Node(int vertex,int color){
        this.vertex=vertex;
        this.color=color;
    }
}
class Solution {
    public static boolean solve(int u,int curCol,int []color,int [][]adj){
        Queue<Node> t=new LinkedList<>();
        color[u]=curCol;
        t.add(new Node(u,curCol));
        while(t.size()>0){
            Node n=t.poll();
            int temU=n.vertex;
            int temCol=n.color;
            for(int v:adj[temU]){
                if(color[v]==temCol){
                    return false;
                }
                if(color[v]==-1){
                    color[v]=1-temCol;
                    t.add(new Node(v,color[v]));
                }
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