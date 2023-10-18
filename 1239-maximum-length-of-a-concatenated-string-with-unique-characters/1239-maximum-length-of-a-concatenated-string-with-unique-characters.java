class Solution {
    public static boolean unique(String s,String t){
        int check[]=new int[26];
        for(int i=0;i<s.length();i++){
            int x=((int)s.charAt(i))-97;
            if(check[x]>0){
                return false;
            }
            check[x]++;
        }
        for(int i=0;i<t.length();i++){
            int x=((int)t.charAt(i))-97;
            if(check[x]>0){
                return false;
            }
            check[x]++;
        }
        return true;
        
    }
    public static int solve(int ind,List<String> arr,String temp,Integer []dp){
        if(ind<0){
            return 0;
        }
        // if(dp[ind]!=null){
        //     return dp[ind];
        // }
        int take=Integer.MIN_VALUE;
        int notTake=Integer.MIN_VALUE;
        if(unique(temp,arr.get(ind))){
            take=arr.get(ind).length()+Solution.solve(ind-1,arr,temp+arr.get(ind),dp);
            notTake=Solution.solve(ind-1,arr,temp,dp);
        }else{
            notTake=Solution.solve(ind-1,arr,temp,dp);
        }
        // dp[ind]=Math.max(take,notTake);
        // return dp[ind];
        return Math.max(take,notTake);
    }
    public int maxLength(List<String> arr) {
        int n=arr.size();
        Integer []dp=new Integer[n];
        return Solution.solve(n-1,arr,"",dp);
        
    }
}