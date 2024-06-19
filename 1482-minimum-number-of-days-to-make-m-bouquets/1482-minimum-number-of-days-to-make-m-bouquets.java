class Solution {
    public boolean traverse(int day,int []bloomDay,int m,int k){
        int i=0,count=0,n=bloomDay.length;
        int adjCount=0;
        while(i<n){
            if(bloomDay[i]>day){
                adjCount=0;
            }else{
                adjCount++;
            }
            if(adjCount==k){
                count++;
                adjCount=0;
            }
            if(count==m)
                return true;
            i++;
        }
        if(count>=m)
            return true;
        return false;
    }
    public int minDays(int[] bloomDay, int m, int k) {
        int n=bloomDay.length;
        int start=1,end=0;
        for(int x:bloomDay){
            end=Math.max(end,x);
        }
        int ans=-1;
        while(start<=end){
            int mid=start-((start-end)/2);
            if(traverse(mid,bloomDay,m,k)){
                ans=mid;
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return ans;
        
    }
}