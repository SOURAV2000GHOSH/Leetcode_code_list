import java.util.HashMap;
class Solution {
    public int minimumRounds(int[] tasks) {
        HashMap<Integer,Integer> check=new HashMap<>();
        for(int a:tasks){
            if(check.containsKey(a)){
                check.put(a,check.get(a)+1);
            }
            else{
                check.put(a,1);
            }
        }
        int round=0;
        for(int i:check.keySet()){
            int count=check.get(i);
            if(count==1)
                return -1;
            if(count%3==0){
                round+=(count/3);
            }
            else{
                round+=(count/3)+1;
            }
        }
        return round;
    }
}