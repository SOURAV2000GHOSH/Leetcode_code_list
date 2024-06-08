class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> mp=new HashMap<>();
        mp.put(0,-1);
        int total=0;
        for(int i=0;i<nums.length;i++){
            total+=nums[i];
            int rem=total%k;
            if(!mp.containsKey(rem)){
                mp.put(rem,i);
            }else if((i-mp.get(rem))>=2){
                 return true; 
            }
        }
        return false;
    }
}