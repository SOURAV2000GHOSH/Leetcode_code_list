class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> mp=new HashMap<>();
        int n=nums.length;
        for(int i=0;i<n;i++){
            mp.put(nums[i],i);
        }
        int []ans={-1,-1};
        for(int i=0;i<n;i++){
            if(mp.containsKey(target-nums[i])){
                if(i==mp.get(target-nums[i])){
                    continue;
                }
                ans[0]=i;
                ans[1]=mp.get(target-nums[i]);
                return ans;
            }
        }
        return ans;
    }
}