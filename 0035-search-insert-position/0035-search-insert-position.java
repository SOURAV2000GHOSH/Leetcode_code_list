class Solution {
    public int searchInsert(int[] nums, int target) {
        int l=0,h=nums.length-1,m;
        int ans=nums.length;
        while(l<=h){
            m=(h+l)/2;
            if(nums[m]>=target){
                ans=m;
                h=m-1;
                
            }else{
                l=m+1;
            }
        }
        return ans;
    }
}