class Solution {
    public int findIndex(int n,int k){
        if(n==1){
            return 0;
        }
        int idx=findIndex(n-1,k);
        idx=(idx+k)%n;
        return idx;
    }
    public int findTheWinner(int n, int k) {
        return findIndex(n,k)+1;
    }
}