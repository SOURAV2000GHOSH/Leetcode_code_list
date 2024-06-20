class Solution {
    public void dfs(ArrayList<ArrayList<Integer>> adj,boolean []visited,int u){
        visited[u]=true;
        for(int v:adj.get(u)){
            if(!visited[v]){
                dfs(adj,visited,v);
            }
        }
    }
    
    public void bfs(ArrayList<ArrayList<Integer>> adj,boolean []visited,int u){
        Queue<Integer> q=new LinkedList<>();
        q.add(u);
        while(q.size()>0){
            int tempU=q.remove();
            if(visited[tempU]){
                continue;
            }
            visited[tempU]=true;
            for(int v:adj.get(tempU)){
                if(!visited[v])
                    q.add(v);
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
                // dfs(adj,visited,i);
                bfs(adj,visited,i);
                count++;
            }
        }
        return count;
        
    }
}