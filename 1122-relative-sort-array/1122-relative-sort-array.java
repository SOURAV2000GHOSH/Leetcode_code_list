class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        TreeMap<Integer,Integer> mp=new TreeMap<>();
        for(int n:arr1){
            if(mp.containsKey(n)){
                mp.put(n,mp.get(n)+1);
            }else{
                mp.put(n,1);
            }
        }
        int []ans=new int[arr1.length];
        int i=0;
        for(int n:arr2){
            int count=mp.get(n);
            mp.remove(n);
            while(count>0){
                ans[i]=n;
                i++;
                count--;
            }
        }
        while(mp.size()>0){
            int key=mp.firstKey();
            int count=mp.get(key);
            mp.remove(key);
            while(count>0){
                ans[i]=key;
                i++;
                count--;
            }
        }
        return ans;
    }
}