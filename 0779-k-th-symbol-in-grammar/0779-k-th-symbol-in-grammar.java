class Solution {
    public static int solve(int n,int k){
        if(n==1 && k==1){
            return 0;
        }
        int t=Solution.solve(n-1,(int)Math.ceil(k/2.0));
        if(t==0){
            if(k%2==0){
                return 1;
            }else{
                return 0;
            }
        }else{
            if(k%2==1){
                return 1;
            }else{
                return 0;
            }
        }
    }
    public int kthGrammar(int n, int k) {
        return Solution.solve(n,k);
        
    }
}