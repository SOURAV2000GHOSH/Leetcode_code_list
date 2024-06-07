class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        String []s=sentence.split(" ");
        StringBuilder ans=new StringBuilder();
        int maxLen=0;
        
        HashMap<String,Integer> mp=new HashMap<>();
        for(String str:dictionary){
            maxLen=Math.max(maxLen,str.length());
            if(mp.containsKey(str)){
                mp.put(str,mp.get(str)+1);
            }else{
                mp.put(str,1);
            }
        }
        for(String str:s){
            int i=0;
            boolean has=false;
            while(i<str.length() && i<=maxLen){
                if(mp.containsKey(str.substring(0,i))){
                    ans.append(str.substring(0,i));
                    ans.append(" ");
                    has=true;
                    break;
                }
                i++;
            }
            if(!has){
                ans.append(str);
                ans.append(" ");
            }
        }
        
        return ans.substring(0,ans.length()-1);
    }
}