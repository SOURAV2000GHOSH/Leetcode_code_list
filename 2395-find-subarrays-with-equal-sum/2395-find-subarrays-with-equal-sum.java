class Solution {
    public boolean findSubarrays(int[] nums) {
        HashSet<Integer> mp=new HashSet<>();
        for(int i=1;i<nums.length;i++){
            if(mp.contains(nums[i]+nums[i-1])){
                return true;
            }else{
                mp.add(nums[i]+nums[i-1]);
            }
        }
        return false;
    }
}