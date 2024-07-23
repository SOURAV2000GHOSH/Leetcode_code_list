class Solution {
    public int[] frequencySort(int[] nums) {
        HashMap<Integer,Integer> mp= new HashMap<>();
        // storing count on elements
        for(int x: nums){
            if(mp.containsKey(x)){
                mp.put(x,mp.get(x)+1);
            }else{
                mp.put(x,1);
            }
        }
        
        List<Integer> store=new ArrayList<>();
        for(int x: nums){
            store.add(x);
        }
        // sorting based on condition
        Collections.sort(store,(a,b)->{
            // checking for frequence
            if(mp.get(a)!=mp.get(b)){
                return mp.get(a)-mp.get(b);
            }
            // checking for sort in decreasing order
            else{
                return b-a;
            }
        });
        
        int []ans = new int[store.size()];
        for(int i=0;i<store.size();i++){
            ans[i]=store.get(i);
        }
        return ans;
    }
}