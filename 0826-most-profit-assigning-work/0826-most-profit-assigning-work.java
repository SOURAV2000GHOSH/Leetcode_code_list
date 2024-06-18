//use for storing purposes
class Node{
    int diference,profit;
    public Node(int diference,int profit){
        this.diference=diference;
        this.profit=profit;
    }
}

class Solution {
    public int solve(List<Node> store,int ind){
        int ans=0;
        int start=0,end=store.size()-1;
        /*doing binary search to get at that 
        index worker can work and we will get max profit*/
        while(start<=end){
            int mid=start-((start-end)/2);
            Node temp=store.get(mid);
            if(temp.diference<=ind){
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
        //sorting based on difference
        Collections.sort(store,(a,b)->a.diference-b.diference);
        //use prefix sum to store maximum profit at that index from starting
        for(int i=1;i<store.size();i++){
            int maxProfit=Math.max(store.get(i).profit,store.get(i-1).profit);
            store.get(i).profit=maxProfit;
        }
        
        //calculating answer
        int ans=0;
        for(int x:worker){
            int temp=solve(store,x);
            ans+=temp;
        }
        return ans;
    }
}