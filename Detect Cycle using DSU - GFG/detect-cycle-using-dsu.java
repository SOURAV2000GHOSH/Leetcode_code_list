//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>>adj = new ArrayList<>();
            for(int i = 0; i < V; i++)
                adj.add(i, new ArrayList<Integer>());
            for(int i = 0; i < E; i++){
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            Solution obj = new Solution();
            int ans = obj.detectCycle(V, adj);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


class Solution
{
    //Function to detect cycle using DSU in an undirected graph.
    public static int findParent(int i,int []parent){
        if(parent[i]==i){
            return i;
        }
        parent[i]=Solution.findParent(parent[i],parent);
        return parent[i];
    }
    public static void union(int x,int y,int []parent,int []rank){
        int parent_x=Solution.findParent(x,parent);
        int parent_y=Solution.findParent(y,parent);
        if(parent_x==parent_y){
            return;
        }
        if(rank[parent_x]==rank[parent_y]){
            parent[parent_y]=parent_x;
            rank[parent_x]++;
        }
        else if(rank[parent_x]>rank[parent_y]){
            parent[parent_y]=parent_x;
        }else{
            parent[parent_x]=parent_y;
        }
    }
    public int detectCycle(int V, ArrayList<ArrayList<Integer>> adj)
    {
        // Code here
        int []parent=new int[V];
        int []rank=new int[V];
        for(int i=0;i<V;i++){
            parent[i]=i;
        }
        for(int u=0;u<V;u++){
            for(int v:adj.get(u)){
                if(u<v){
                    int uParent=Solution.findParent(u,parent);
                    int vParent=Solution.findParent(v,parent);
                    if(uParent==vParent){
                        return 1;
                    }else{
                        Solution.union(u,v,parent,rank);
                    }
                }
            }
        }
        return 0;
        
    }
}
















