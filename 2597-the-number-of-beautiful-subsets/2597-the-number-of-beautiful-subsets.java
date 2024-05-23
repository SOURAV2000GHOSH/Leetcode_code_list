class Solution {
    public boolean check(List<Integer> store,int k){
        int l=store.size();
        if(l==0)
            return false;
        else if(l==1)
            return true;
        for(int i=0;i<l;i++){
            for(int j=i+1;j<l;j++){
                if(Math.abs(store.get(j)-store.get(i))==k)
                    return false;
            }
        }
        return true;
    }
    
    public void backtrack(int ind,int k,int n,int[] ans,List<Integer> store,int[] nums){
        if(ind==n){
            if(check(store,k)){
                ans[0]+=1;
            }
            return;
        }
        store.add(nums[ind]);
        backtrack(ind+1,k,n,ans,store,nums);
        store.removeLast();
        backtrack(ind+1,k,n,ans,store,nums);
    }
    public int beautifulSubsets(int[] nums, int k) {
        List<Integer> store=new ArrayList<>();
        int []ans={0};
        backtrack(0,k,nums.length,ans,store,nums);
        return ans[0];
        
    }
}