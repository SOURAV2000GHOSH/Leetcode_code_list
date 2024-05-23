class Solution {
    public static int ans;
    public void backtrack(int ind,int n,int k,int []nums,Set<Integer> store){
        if(ind>=n){
            Solution.ans++;
            return;
        }
        backtrack(ind+1,n,k,nums,store);
        
        if(!store.contains(nums[ind]+k) && !store.contains(nums[ind]-k)){
            store.add(nums[ind]);
            backtrack(ind+1,n,k,nums,store);
            store.remove(nums[ind]);
        }
        
    }
    public int beautifulSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        Set<Integer> store=new HashSet<>();    
        Solution.ans=0;
        backtrack(0,nums.length,k,nums,store);
        return ans-1;
    }
}