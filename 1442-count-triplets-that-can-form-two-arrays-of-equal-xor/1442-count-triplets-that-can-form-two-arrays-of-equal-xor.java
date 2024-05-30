class Solution {
    public int countTriplets(int[] arr) {
        int n=arr.length,count=0;
        int prefixSum[]=new int[n+1];
        for(int i=0;i<n;i++){
            prefixSum[i+1]=prefixSum[i]^arr[i];
        }
        for(int i=0;i<=n;i++){
            for(int j=i+1;j<=n;j++){
                if(prefixSum[i]==prefixSum[j]){
                    count+=(j-i-1);
                }
            }
        }
        return count;
    }
}