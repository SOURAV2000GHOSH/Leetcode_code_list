class Solution {
    public boolean traverse(int min,int []arr,int m){
        int ball=1;
        int prev=arr[0];
        for(int i=1;i<arr.length;i++){
            if((arr[i]-prev)>=min){
                prev=arr[i];
                ball++;
                if(ball==m)
                    return true;
            }
        }
        return false;
    }
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int start=1,end=position[position.length-1],ans=0;
        while(start<=end){
            int mid=start-((start-end)/2);
            if(traverse(mid,position,m)){
                ans=mid;
                start=mid+1;
            }else{
                end=mid-1;
            }
        }
        return ans;
        
    }
}