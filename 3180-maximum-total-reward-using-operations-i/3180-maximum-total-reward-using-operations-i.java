class Solution {
    public int dp(int i,int []arr,int reward,int [][]store,int n){
        if(i>=n){
            return 0;
        }
        if(-1 != store[i][reward]){
            return store[i][reward];
        }
        int a=0;
        if(arr[i]>reward){
            a=arr[i]+dp(i+1,arr,reward+arr[i],store,n);
        }
        int b=dp(i+1,arr,reward,store,n);
        store[i][reward]=Math.max(a,b);
        return store[i][reward];
    }
    
    public int maxTotalReward(int[] arr) {
        Arrays.sort(arr);
        int n=arr.length;
        int[][] store=new int[n][4000];
        for(int i=0;i<n;i++){
            Arrays.fill(store[i],-1);
        }
        return dp(0,arr,0,store,n);
       
    }
}