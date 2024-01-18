class Solution {
    public int []dp;
    public int solve(int n){
        if(n<3){
            return n;
        }
        if(dp[n]!=0){
            return dp[n];
        }
        int takeOne=solve(n-1);
        int takeTwo=solve(n-2);
        dp[n]=takeOne+takeTwo;
        return dp[n];
    }
    public int climbStairs(int n) {
        dp=new int[n+1];
        return solve(n);
    }
}