class Solution {
    public int subarraySum(int[] nums, int k) {
        int cumilativeSum=0;
        int count=0;
        HashMap<Integer,Integer> mp=new HashMap<>();
        mp.put(0,1);
        for(int n:nums){
            cumilativeSum+=n;
            if(mp.containsKey(cumilativeSum-k)){
                count+=mp.get(cumilativeSum-k);
            }
            if(mp.containsKey(cumilativeSum)){
                mp.put(cumilativeSum,mp.get(cumilativeSum)+1);
            }else{
                mp.put(cumilativeSum,1);
            }
        }
        return count;
    }
}