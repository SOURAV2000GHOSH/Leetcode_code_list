class Solution {
    public int[] searchRange(int[] nums, int target) {
        int []ans={-1,-1};
        int s=0;
        int e=nums.length-1;
        while(s<=e){
            int mid=(s+e)/2;
            if(nums[mid]==target){
                ans[0]=mid;
                ans[1]=mid;
                break;
            }else if(nums[mid]<target){
                s=mid+1;
            }else{
                e=mid-1;
            }
        }
            if(ans[0]!=-1){
                while(ans[0]>0 && nums[ans[0]-1]==nums[ans[0]]){
                    ans[0]-=1;            
                }
            }
        if(ans[1]!=-1){
            while(ans[1]<nums.length-1 && nums[ans[1]]==nums[ans[1]+1]){
                ans[1]+=1;
            }
        }
        return ans;
    }
}