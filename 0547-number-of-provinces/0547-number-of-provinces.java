class Solution {
    public void traverse(ArrayList<ArrayList<Integer>> adj,boolean []visited,int u){
        visited[u]=true;
        for(int v:adj.get(u)){
            if(!visited[v]){
                traverse(adj,visited,v);
            }
        }
    }
    
    public int findCircleNum(int[][] isConnected) {
        int count=0;
        int n=isConnected.length;
        boolean []visited=new boolean[n];
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<n;i++){
            adj.add(new ArrayList<>());
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(isConnected[i][j]==1){
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }
        for(int i=0;i<n;i++){
            if(!visited[i]){
                traverse(adj,visited,i);
                count++;
            }
        }
        return count;
        
    }
}