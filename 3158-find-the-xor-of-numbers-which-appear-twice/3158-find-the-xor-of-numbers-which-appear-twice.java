class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        Arrays.sort(nums);
        int ans=0;
        int temp=0;
        for(int n:nums){
            if((temp^n)==0){
                ans^=n;
                temp=0;
            }else{
                temp=n;
            }
        }
        return ans;
        
    }
}