class Solution {
    public static int lcs(String s1,String s2){
        int l=s1.length();
        int [][]dp=new int[l+1][l+1];
        for(int i=1;i<=l;i++){
            for(int j=1;j<=l;j++){
                int match=Integer.MIN_VALUE;
                int notMatch=Integer.MIN_VALUE;
                if(s1.charAt(i-1)==s2.charAt(j-1)){
                    match=1+dp[i-1][j-1];
                }
                else{
                    notMatch=Math.max(dp[i][j-1],dp[i-1][j]);
                }
                dp[i][j]=Math.max(match,notMatch);
            }
        }
        return dp[l][l];
        
    }
    public int longestPalindromeSubseq(String s) {
        char []arr=s.toCharArray();
        int i=0,j=s.length()-1;
        while(i<j){
            char temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            i++;
            j--;
        }
        // System.out.println(new String(arr));
        return Solution.lcs(s,new String(arr));
    }
}