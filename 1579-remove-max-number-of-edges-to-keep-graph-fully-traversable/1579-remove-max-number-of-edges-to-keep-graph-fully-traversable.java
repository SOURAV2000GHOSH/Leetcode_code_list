class DSU{
    public int []parent;
    public int []rank;
    public int component;
    public DSU(int n){
        parent = new int[n+1];
        rank=new int[n+1];
        for(int i=1;i<=n;i++){
            parent[i]=i;
        }
        this.component=n;
    }
    public int find(int i){
        if(parent[i]==i)
            return i;
        return parent[i]=find(parent[i]);
    }   
    public void union(int a, int b){
        int parentA=find(a);
        int parentB=find(b);
        if(parentA==parentB)
            return;
        if(rank[parentA]<rank[parentB]){
          parent[parentA]=parentB;  
        }else if(rank[parentA]>rank[parentB]){
            parent[parentB]=parentA;
        }else{
            parent[parentA]=parentB;
            rank[parentB]++;
        }
        this.component--;
    }
    
    public boolean isOneComponent(){
        return this.component==1;
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        DSU alice = new DSU(n);
        DSU bob=new DSU(n);
        Arrays.sort(edges,(a,b)->b[0]-a[0]);
        int edgeCount=0;
        for(int []arr:edges){
            int type=arr[0];
            int u=arr[1];
            int v=arr[2];
            if(type==3){
                boolean isAdd=false;
                // adding for alice
                if(alice.find(u)!=alice.find(v)){
                    alice.union(u,v);
                    isAdd=true;
                }
                // adding for bob
                if(bob.find(u)!=bob.find(v)){
                    bob.union(u,v);
                    isAdd=true;
                }
                if(isAdd){
                   edgeCount++; 
                }
            }else if(type==2){
                if(bob.find(u)!=bob.find(v)){
                    bob.union(u,v);
                    edgeCount++;
                }
            }else{
                if(alice.find(u)!=alice.find(v)){
                    alice.union(u,v);
                    edgeCount++;
                }
            }
        }
        if(alice.isOneComponent() && bob.isOneComponent()){
            return edges.length-edgeCount;
        }
            
        return -1;
    }
}