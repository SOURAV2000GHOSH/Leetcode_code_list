class Solution {
    public static int lcs(int ind1,int ind2,String a,String b,Integer [][]dp){
        if(ind1<0 || ind2<0){
            return 0;
        }
        if(dp[ind1][ind2]!=null){
            return dp[ind1][ind2];
        }
        int match=Integer.MIN_VALUE;
        int notMatch=Integer.MIN_VALUE;
        if(a.charAt(ind1)==b.charAt(ind2)){
            match=1+Solution.lcs(ind1-1,ind2-1,a,b,dp);
        }else{
            notMatch=Math.max(Solution.lcs(ind1-1,ind2,a,b,dp),Solution.lcs(ind1,ind2-1,a,b,dp));
        }
        dp[ind1][ind2]=Math.max(match,notMatch);
        return dp[ind1][ind2];
    }
    public int minInsertions(String s) {
        char []temp=s.toCharArray();
        int l=s.length();
        int st=0,e=l-1;
        while(st<e){
            char t=temp[st];
            temp[st]=temp[e];
            temp[e]=t;
            st++;
            e--;
        }
        Integer [][]dp=new Integer[l][l];
        int ans=Solution.lcs(l-1,l-1,s,new String(temp),dp);
        return l-ans;
        
    }
}