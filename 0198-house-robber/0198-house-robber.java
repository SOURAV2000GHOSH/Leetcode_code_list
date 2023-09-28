import java.util.Arrays;
class Solution {
    public static int solve(int ind, int []arr,int []dp){
		if(ind==0){
			return arr[0];
		}
		if(ind<0){
			return 0;
		}
		if(dp[ind]!=-1){
			return dp[ind];
		}
		int pick=Solution.solve(ind-2, arr, dp)+arr[ind];
		int notPick=Solution.solve(ind-1, arr, dp);
		dp[ind]=Math.max(pick, notPick);
		return dp[ind];
	}
    
    public int rob(int[] nums) {
        int l=nums.length;
        int []dp=new int[l];
        Arrays.fill(dp,-1);
        return Solution.solve(l-1,nums,dp);
        
    }
}