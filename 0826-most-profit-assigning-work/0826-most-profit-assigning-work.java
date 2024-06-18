class Node{
    int dif,profit;
    public Node(int dif,int profit){
        this.dif=dif;
        this.profit=profit;
    }
}
class Solution {
    public int solve(List<Node> store,int ind){
        int ans=0;
        int start=0,end=store.size()-1;
        while(start<=end){
            int mid=start-((start-end)/2);
            Node temp=store.get(mid);
            if(temp.dif<=ind){
                ans=temp.profit;
                start=mid+1;
            }else{
                end=mid-1;
            }
        }
        return ans;
    }
    
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        List<Node> store =new ArrayList<>();
        int n=difficulty.length;
        for(int i=0;i<n;i++){
            store.add(new Node(difficulty[i],profit[i]));
        }
        Collections.sort(store,(a,b)->{
            if(a.dif!=b.dif){
                return a.dif-b.dif;
            }else{
                return a.profit-b.profit;
            }
        });
        int maxProfit=0;
        for(int i=0;i<store.size();i++){
            Node temp=store.get(i);
            maxProfit=Math.max(temp.profit,maxProfit);
            temp.profit=maxProfit;
        }
        int ans=0;
        for(int x:worker){
            int temp=solve(store,x);
            ans+=temp;
        }
        return ans;
    }
}