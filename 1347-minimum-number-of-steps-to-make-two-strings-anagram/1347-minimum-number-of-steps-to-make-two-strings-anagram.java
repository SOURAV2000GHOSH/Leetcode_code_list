class Solution {
    public int minSteps(String s, String t) {
        HashMap<Character,Integer> sh=new HashMap<>();
        HashMap<Character,Integer> th=new HashMap<>();
        for(int i=0;i<s.length();i++){
            Character c=s.charAt(i);
            if(sh.containsKey(c)){
                sh.put(c,sh.get(c)+1);
            }else{
                sh.put(c,1);
            }
        }
        
        for(int i=0;i<t.length();i++){
            Character c=t.charAt(i);
            if(th.containsKey(c)){
                th.put(c,th.get(c)+1);
            }else{
                th.put(c,1);
            }
        }
        int ans=0;
        for(Map.Entry<Character,Integer> m:sh.entrySet()){
            Character k=m.getKey();
            Integer v=m.getValue();
            if(!th.containsKey(k)){
                ans+=v;
            }else{
                if(v>th.get(k)){
                    ans+=(v-th.get(k));
                }
            }
        }
        return ans;
    }
}