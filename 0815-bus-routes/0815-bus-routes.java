import java.util.*;
class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if(source==target){
            return 0;
        }
        Queue<Integer> q=new LinkedList<>();
        HashMap<Integer,ArrayList<Integer>> store=new HashMap<>();
        int n=routes.length;
        boolean []visited=new boolean[n];
        for(int i=0;i<n;i++){
            for(int a:routes[i]){
                if(store.containsKey(a)){
                    ArrayList<Integer> te=store.get(a);
                    te.add(i);
                    store.put(a,te);
                }else{
                    ArrayList<Integer> t=new ArrayList<>();
                    t.add(i);
                    store.put(a,t);
                }
                if(a==source){
                    q.add(i);
                    visited[i]=true;
                }
            }
        }
        int count=1;
        while(q.size()>0){
            int len=q.size();
            while(len!=0){
                len--;
                int bus=q.poll();
                for(int route:routes[bus]){
                    if(route==target)
                        return count;
                    for(int b:store.get(route)){
                        if(!visited[b]){
                            visited[b]=true;
                            q.add(b);
                        }
                    }
                } 
            }
            count++;
        }
        return -1;
    }
}