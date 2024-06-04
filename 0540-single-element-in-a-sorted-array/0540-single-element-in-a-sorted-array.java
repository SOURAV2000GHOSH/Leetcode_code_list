class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n=nums.length;
        int start=0,end=n-1;
        //handling corner case
        if(n==1){
            return nums[0];
        }else if(nums[0]!=nums[1]){
            return nums[0];
        }else if(nums[n-1]!=nums[n-2]){
            return nums[n-1];
        }
        
        while(start<=end){
            int mid=start-((start-end)/2);
            if(nums[mid]!=nums[mid-1] && nums[mid]!=nums[mid+1]){
                return nums[mid];
            }
            else if(nums[mid]==nums[mid-1]){
                if(mid%2==1){
                    start=mid+1;
                }else{
                    end=mid-1;
                }
            }else{
                if(mid%2==0){
                    start=mid+1;
                }else{
                    end=mid-1;
                }
            }
        }
        return -1;
        
    }
}