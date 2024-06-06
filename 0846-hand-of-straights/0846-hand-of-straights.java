class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n=hand.length;
        if(n%groupSize!=0)
            return false;
        TreeMap<Integer,Integer> mp= new TreeMap<>();
        for(int x:hand){
            if(mp.containsKey(x)){
                mp.put(x,mp.get(x)+1);
            }else{
                mp.put(x,1);
            }
        }
        while(mp.size()>0){
            int prev=mp.firstKey();
            mp.put(prev,mp.get(prev)-1);
            if(mp.get(prev)==0){
                mp.remove(prev);
            }
            int count=1;
            while(count<groupSize){
                int cur=prev+1;
                if(!mp.containsKey(cur)){
                    return false;
                }  
                mp.put(cur,mp.get(cur)-1);
                if(mp.get(cur)==0){
                    mp.remove(cur);
                }
                prev=cur;
                count++;
            }        
        }
        return true;
        
    }
}