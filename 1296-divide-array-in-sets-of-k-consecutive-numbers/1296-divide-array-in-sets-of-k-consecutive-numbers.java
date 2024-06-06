class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        if(nums.length%k!=0){
            return false;
        }
        TreeMap<Integer,Integer> mp = new TreeMap<>();
        for(int n:nums){
            if(mp.containsKey(n)){
                mp.put(n,mp.get(n)+1);
            }else{
                mp.put(n,1);
            }
        }
        while(mp.size()>0){
            int prev=mp.firstKey();
            mp.put(prev,mp.get(prev)-1);
            if(mp.get(prev)==0){
                mp.remove(prev);
            }
            int count=1;
            while(count<k){
                int cur=prev+1;
                if(!mp.containsKey(cur)){
                    return false;
                }
                mp.put(cur,mp.get(cur)-1);
                if(mp.get(cur)==0){
                    mp.remove(cur);
                }
                count++;
                prev=cur;
            }
        }
        return true;
        
    }
}