class Solution {
    public static int solve(int []coins,int amount,Integer []dp){
        if(amount==0){
            return 0;
        }
        if(dp[amount]!=null){
            return dp[amount];
        }
        int count=1000000000;
        for(int coin:coins){
            if(amount-coin>=0){
                count=Math.min(count,1+Solution.solve(coins,amount-coin,dp));
            }
        }
        dp[amount]=count;
        return count;
    }
    public int coinChange(int[] coins, int amount) {
        int n=coins.length;
        Integer []dp=new Integer[amount+1];
        int ans=Solution.solve(coins,amount,dp);
        if(ans==1000000000){
            return -1;
        }
        return ans;
    }
}