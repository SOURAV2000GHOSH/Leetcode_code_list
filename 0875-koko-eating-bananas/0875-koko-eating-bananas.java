class Solution {
    public long takeTime(int []piles,int n){
        long ans=0;
        for(int x:piles){
            ans+=(long)Math.ceil((x*1.0d)/n);
        }
        return ans;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int start=1,end=Integer.MIN_VALUE;
        int ans=0;
        for(int n:piles){
            end=Math.max(end,n);
        }
        while(start<=end){
            int mid=start-((start-end)/2);
            long time=takeTime(piles,mid);
            if(time<=h){
                ans=mid;
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return ans;
    }
}