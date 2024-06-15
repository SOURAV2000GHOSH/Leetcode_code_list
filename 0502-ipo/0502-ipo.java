class Node{
    int capital,profit;
    public Node(int capital,int profit){
        this.capital=capital;
        this.profit=profit;
    }
}

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Node> pq=new PriorityQueue<>((a,b)->(b.profit-a.profit));     
        List<Node> store=new ArrayList<>();
        for(int i=0;i<profits.length;i++){
            store.add(new Node(capital[i],profits[i]));
        }
        Collections.sort(store,(a,b)->{
        return a.capital-b.capital;});
        int i=0;
        while(i<store.size() && k>0){
            Node temp=store.get(i);
            if(temp.capital<=w){
                pq.add(temp);
            }else if(pq.size()>0){
                Node first=pq.poll();
                w+=first.profit;
                k--;
                continue;
            }
            i++;
        }
        while(k>0 && pq.size()>0){
            Node first=pq.poll();
            w+=first.profit;
            k--;
        }
        return w;
    }
}