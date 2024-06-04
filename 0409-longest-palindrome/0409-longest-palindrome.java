class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character,Integer> store = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(store.containsKey(c)){
                store.put(c,store.get(c)+1);
            }else{
                store.put(c,1);
            }
        }
        int ans=0;
        boolean haveOne=true;
        
        for(Map.Entry<Character,Integer> map: store.entrySet()){
            Integer val=map.getValue();
            if(val==1 && haveOne){
                ans+=1;
                haveOne=false;
            }
            if(val>1){
                if(val%2==0){
                    ans+=val;
                }else{
                    ans+=(val-1);
                    if(haveOne){
                        ans+=1;
                        haveOne=false;
                    }
                }
            }
        }
        return ans;
    }
}