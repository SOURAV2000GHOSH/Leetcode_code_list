class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer,Integer> mp=new HashMap<>();
        List<Integer> store = new ArrayList<>();
        for(int n:nums1){
            if(mp.containsKey(n)){
                mp.put(n,mp.get(n)+1);
            }else{
                mp.put(n,1);
            }
        }
        for(int n:nums2){
            if(mp.containsKey(n)){
                store.add(n);
                mp.put(n,mp.get(n)-1);
                if(mp.get(n)==0){
                    mp.remove(n);
                }
            }
        }
        int []ans=new int[store.size()];
        for(int i=0;i<store.size();i++){
            ans[i]=store.get(i);
        }
        return ans;
    }
}
