//{ Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class DriverClass
{
    public static void main(String args[]) throws IOException {

        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String str[] = read.readLine().trim().split(" ");
            int V = Integer.parseInt(str[0]);
            int E = Integer.parseInt(str[1]);
    
            ArrayList<ArrayList<ArrayList<Integer>>> adj = new ArrayList<ArrayList<ArrayList<Integer>>>();
            for(int i=0;i<V;i++)
            {
                adj.add(new ArrayList<ArrayList<Integer>>());
            }
            
            int i=0;
            while (i++<E) {
                String S[] = read.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                int w = Integer.parseInt(S[2]);
                ArrayList<Integer> t1 = new ArrayList<Integer>();
                ArrayList<Integer> t2 = new ArrayList<Integer>();
                t1.add(v);
                t1.add(w);
                t2.add(u);
                t2.add(w);
                adj.get(u).add(t1);
                adj.get(v).add(t2);
            }
            
            int S = Integer.parseInt(read.readLine());
            
            Solution ob = new Solution();
            
            int[] ptr = ob.dijkstra(V, adj, S);
            
            for(i=0; i<V; i++)
                System.out.print(ptr[i] + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Node implements Comparable<Node>{
    int distance;
    int nodeVal;
    public Node(int d,int n){
        distance=d;
        nodeVal=n;
    }
    @Override
    public int compareTo(Node n){
        return this.distance-n.distance;
    }
}

class Solution
{
    //Function to find the shortest distance of all the vertices
    //from the source vertex S.
    static int[] dijkstra(int V, ArrayList<ArrayList<ArrayList<Integer>>> adj, int S)
    {
        // Write your code here
        Queue<Node> pq=new PriorityQueue<>();
        int []dist=new int[V];
        Arrays.fill(dist,10000000);
        dist[S]=0;
        pq.add(new Node(0,S));
        while(pq.size()>0){
            Node n=pq.poll();
            int u=n.nodeVal,d=n.distance;
            for(ArrayList<Integer> arr:adj.get(u)){
                int tempD=arr.get(1)+d,v=arr.get(0);
                if(dist[v]>tempD){
                    dist[v]=tempD;
                    pq.add(new Node(tempD,v));
                }
            }
        }
        return dist;
    }
}

