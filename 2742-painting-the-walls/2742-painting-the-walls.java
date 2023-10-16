class Solution {
    public static int solve(int ind,int n,int remain,int []cost,int []time,Integer [][]dp){
        
        if(remain<=0){
            return 0;
        }
        if(ind>=n){
            return 1000000000;
        }
        if(dp[ind][remain]!=null){
            return dp[ind][remain];
        }
        int paint=cost[ind]+Solution.solve(ind+1,n,remain-1-time[ind],cost,time,dp);
        int notPaint=Solution.solve(ind+1,n,remain,cost,time,dp);
        dp[ind][remain]=Math.min(paint,notPaint);
        return dp[ind][remain];
    }
    public int paintWalls(int[] cost, int[] time) {
        int n=cost.length;
        Integer [][]dp=new Integer[n+1][n+1];
        return Solution.solve(0,n,n,cost,time,dp);
        
    }
}