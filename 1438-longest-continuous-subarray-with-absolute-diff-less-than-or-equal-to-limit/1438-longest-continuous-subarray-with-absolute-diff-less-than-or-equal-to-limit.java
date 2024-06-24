class Node{
    int val,ind;
    public Node(int v,int i){
        val=v;
        ind=i;
    }
}

class Solution {
    public void checkAndRemove(int i,PriorityQueue<Node> pq){
        while(pq.size()>0 && pq.peek().ind<i){
            pq.poll();
        }
    }
    
    public int longestSubarray(int[] nums, int limit) {
        PriorityQueue<Node> minHeap=new PriorityQueue<>((a,b)->{
            if(a.val!=b.val)
                return a.val-b.val;
            return a.ind-b.ind;
        });
        PriorityQueue<Node> maxHeap=new PriorityQueue<>((a,b)->{
            if(a.val!=b.val)
                return b.val-a.val;
            return a.ind-b.ind;
        });
        int i=0,j=0;
        int ans=0,n=nums.length;
        while(i<n && j<n){
            minHeap.add(new Node(nums[j],j));
            maxHeap.add(new Node(nums[j],j));
            Node min=minHeap.peek();
            Node max=maxHeap.peek();
            if(Math.abs(max.val-min.val)<=limit){
                ans=Math.max(ans,(j-i+1));
            }else{
                i=Math.min(min.ind,max.ind)+1;
                checkAndRemove(i,minHeap);
                checkAndRemove(i,maxHeap);
            }
            j++;
        }
        return ans;
    }
}