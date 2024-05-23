class Solution {
    public boolean check(List<Integer> store,int k){
        int l=store.size();
        if(l==0)
            return false;
        else if(l==1)
            return true;
        for(int i=0;i<l;i++){
            for(int j=i+1;j<l;j++){
                if(store.get(j)-store.get(i)==k)
                    return false;
            }
        }
        return true;
    }
    
    public int backtrack(int ind,int k,int n,List<Integer> store,int[] nums){
        if(ind==n){
            if(check(store,k)){
                return 1;
            }
            return 0;
        }
        store.add(nums[ind]);
        int a=backtrack(ind+1,k,n,store,nums);
        store.removeLast();
        int b=backtrack(ind+1,k,n,store,nums);
        return a+b;
    }
    public int beautifulSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        List<Integer> store=new ArrayList<>();    
        return backtrack(0,k,nums.length,store,nums);
        
    }
}