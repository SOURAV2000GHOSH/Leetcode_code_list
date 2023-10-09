import java.util.*;
class Solution {
    public static int findParent(int i,int []parent){
        if(parent[i]==i){
            return i;
        }
        parent[i]=Solution.findParent(parent[i],parent);
        return parent[i];
    }
    public static void union(int x,int y,int []parent,int []rank){
        int parentx=Solution.findParent(x,parent);
        int parenty=Solution.findParent(y,parent);
        if(parentx==parenty){
            return;
        }
        if(rank[parentx]==rank[parenty]){
            parent[parenty]=parentx;
            rank[parentx]++;
        }else if(rank[parentx]>rank[parenty]){
            parent[parenty]=parentx;
        }else{
            parent[parentx]=parenty;
        }
    }
    
    public long countPairs(int n, int[][] edges) {
        int []rank=new int[n];
        int []parent=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        for(int []arr:edges){
            Solution.union(arr[0],arr[1],parent,rank);
        }
        HashMap<Integer,Long> store=new HashMap<>();
        for(int i=0;i<n;i++){
            int p=Solution.findParent(i,parent);
            if(store.containsKey(p)){
                store.put(p,store.get(p)+1L);
            }else{
                store.put(p,1L);
            } 
        }
        long result=0;
        int remaining=n;
        for(Map.Entry<Integer,Long> mp:store.entrySet()){
            Long val=mp.getValue();
            result+=(val*(remaining-val));
            remaining-=val;
        }
        return result;
    }
}




