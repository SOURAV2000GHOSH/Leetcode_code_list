class Solution {
    public static boolean check(int i,int j,String s,Boolean [][]dp){
        if(i>=j){
            return true;
        }
        if(dp[i][j]!=null){
            return dp[i][j];
        }
        if(s.charAt(i)==s.charAt(j)){
            return Solution.check(++i,--j,s,dp);
        }
        return false;
    }
    public String longestPalindrome(String s) {
        int n=s.length();
        Boolean [][]dp=new Boolean[n][n];
        int start=-1,maxLen=0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if((j-i+1)>maxLen && Solution.check(i,j,s,dp)){
                    maxLen=j-i+1;
                    start=i;
                }
            }
        }
        return s.substring(start,start+maxLen);
    }
}