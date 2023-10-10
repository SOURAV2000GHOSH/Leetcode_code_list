class Solution {
    public static int solve(int ind,Integer []dp){
        if(ind==1 || ind==2){
            return ind;
        }
        if(dp[ind]!=null){
            return dp[ind];
        }
        int takeOneStep=Solution.solve(ind-1,dp);
        int takeTwoStep=Solution.solve(ind-2,dp);
        dp[ind]=takeOneStep+takeTwoStep;
        return dp[ind];
    }
    public int climbStairs(int n) {
        Integer []dp=new Integer[n+1];
        return Solution.solve(n,dp);
        
    }
}