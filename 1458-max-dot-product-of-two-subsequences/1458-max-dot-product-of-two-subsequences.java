class Solution {
    public static int solve(int ind1,int ind2,int[] n1,int []n2,Integer [][]dp){
        if(ind1<0 || ind2<0){
            return -100000;
        }
        if(dp[ind1][ind2]!=null){
            return dp[ind1][ind2];
        }
        int onlyThat=n1[ind1]*n2[ind2];
        int thatAndOther=(n1[ind1]*n2[ind2])+Solution.solve(ind1-1,ind2-1,n1,n2,dp);
        int takeFirst=Solution.solve(ind1,ind2-1,n1,n2,dp);
        int takeSecond=Solution.solve(ind1-1,ind2,n1,n2,dp);
        dp[ind1][ind2]=Math.max(onlyThat,Math.max(thatAndOther,Math.max(takeFirst,takeSecond)));
        return dp[ind1][ind2];
    }
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int l1=nums1.length,l2=nums2.length;
        Integer [][]dp=new Integer[l1][l2];
        return Solution.solve(l1-1,l2-1,nums1,nums2,dp);
        
    }
}