class Solution {
    public static int solve(int ind,int amount,int []coins,Integer [][]dp){
        if(ind<0){
            return 0;
        }
        if(amount==0){
            return 1;
        }
        if(dp[ind][amount]!=null){
            return dp[ind][amount];
        }
        int notPick=Solution.solve(ind-1,amount,coins,dp);
        int pick=0;
        if(coins[ind]<=amount){
            pick=Solution.solve(ind,amount-coins[ind],coins,dp);
        }
        dp[ind][amount]=pick+notPick;
        return dp[ind][amount];
    }
    public int change(int amount, int[] coins) {
        int n=coins.length;
        Integer [][]dp=new Integer[n][amount+1];
        int ans=Solution.solve(n-1,amount,coins,dp);
        return ans;
        
    }
}