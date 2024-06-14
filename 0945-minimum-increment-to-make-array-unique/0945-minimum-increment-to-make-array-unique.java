class Solution {
    public int minIncrementForUnique(int[] nums) {
        Arrays.sort(nums);
        int count=0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]<=nums[i-1]){
                int temp=((nums[i-1]-nums[i])+1);
                nums[i]+=temp;
                count+=temp;
            }
            // while(nums[i]<=nums[i-1]){
            //     nums[i]++;
            //     count++;
            // }
        }
        return count;
    }
}