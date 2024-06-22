class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        HashMap<Integer,Integer> mp=new HashMap<>();
        mp.put(0,1);
        int odd=0;
        int ans=0;
        for(int n:nums){
            if(n%2==1){
                odd++;
            }
            if(mp.containsKey(odd-k)){
                ans+=mp.get(odd-k);
            }
            if(mp.containsKey(odd))
                mp.put(odd,mp.get(odd)+1);
            else
                mp.put(odd,1);
        }
        return ans;
    }
}