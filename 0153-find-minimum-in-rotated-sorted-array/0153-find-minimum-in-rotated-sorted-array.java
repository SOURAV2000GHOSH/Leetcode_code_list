class Solution {
    public int findMin(int[] nums) {
        int start=0,end=nums.length-1;
        int ans=nums[0];
        while(start<=end){
            int mid=start-((start-end)/2);
            ans=Math.min(ans,nums[mid]);
            if(nums[mid]<=nums[end]){
                end=mid-1;
            }else{
                start=mid+1;
            }
        }
        return ans;
        
    }
}