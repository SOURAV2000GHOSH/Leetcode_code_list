class Solution {
    public int getXor(int arr[],int start,int end){
        int ans=0;
        for(int i=start;i<=end;i++){
            ans=(ans^arr[i]);
        }
        return ans;
    }
    public int countTriplets(int[] arr) {
        int count=0,n=arr.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                for(int k=j;k<n;k++){
                    int a=getXor(arr,i,j-1);
                    int b=getXor(arr,j,k);
                    if(a==b){
                        count++;
                    }
                }
            }
        }
        return count;
    }
}