class Solution {
    public int countTriplets(int[] arr) {
        int n=arr.length,count=0;
        for(int i=0;i<n;i++){
            int temp=arr[i];
            for(int j=i+1;j<n;j++){
                temp=temp^arr[j];
                if(temp==0){
                    count+=(j-i);
                }
            }
        }
        return count;
        
    }
}