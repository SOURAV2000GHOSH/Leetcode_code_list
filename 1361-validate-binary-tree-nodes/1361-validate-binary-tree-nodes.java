class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        HashMap<Integer,Integer> store=new HashMap<>();
        
        for(int i=0;i<n;i++){
            int l=leftChild[i],r=rightChild[i];
            if(l!=-1){
                if(store.containsKey(l)){
                    return false;
                }
                store.put(l,i);
                
            }
            if(r!=-1){
                if(store.containsKey(r)){
                    return false;
                }
                store.put(r,i);
                
            }
        }
        int root=-1;
        for(int i=0;i<n;i++){
            if(!store.containsKey(i)){
                if(root!=-1){
                    return false;
                }
                root=i;
            }
        }
        if(root==-1){
            return false;
        }
        int nodeCount=0;
        Queue<Integer> q=new LinkedList<>();
        q.add(root);
        while(q.size()>0){
            int i=q.poll();
            nodeCount++;
            int l=leftChild[i],r=rightChild[i];
            if(l!=-1){
                q.add(l);              
            }
            if(r!=-1){
                q.add(r);               
            }
        }
        if(nodeCount!=n){
            return false;
        }
        return true;
        
    }
}