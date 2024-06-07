class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        String []s=sentence.split(" ");
        StringBuilder ans=new StringBuilder();
        int maxLen=0;
        
        HashSet<String> mp=new HashSet<>();
        for(String str:dictionary){
            maxLen=Math.max(maxLen,str.length());
            mp.add(str);
        }
        for(String str:s){
            int i=0;
            boolean hasDictionary=false;
            while(i<str.length() && i<=maxLen){
                if(mp.contains(str.substring(0,i))){
                    ans.append(str.substring(0,i));
                    ans.append(" ");
                    hasDictionary=true;
                    break;
                }
                i++;
            }
            if(!hasDictionary){
                ans.append(str);
                ans.append(" ");
            }
        }
        
        return ans.substring(0,ans.length()-1);
    }
}