class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        HashMap<Integer,Integer> h=new HashMap<>();
        h.put(0,1);
        int total=0,ans=0;
        for(int n:nums){
            total+=n;
            int rem=total%k;
            if(rem<0){
                rem+=k;
            }
            if(h.containsKey(rem)){
                ans+=h.get(rem);
                h.put(rem,h.get(rem)+1);
            }else{
                h.put(rem,1);
            }
        }
        return ans;
    }
}