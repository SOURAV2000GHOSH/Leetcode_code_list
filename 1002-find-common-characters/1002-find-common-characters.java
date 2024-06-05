class Solution {
    public List<String> commonChars(String[] words) {
        int []prev = new int[26];
        for(int i=0;i<words[0].length();i++){
            char c=words[0].charAt(i);
            prev[c-'a']++;
        }
        for(int i=1;i<words.length;i++){
            int []cur = new int[26];
            for(int j=0;j<words[i].length();j++){
                char c=words[i].charAt(j);
                cur[c-'a']++;
            }
            for(int k=0;k<26;k++){
                if(cur[k]==prev[k]){
                    continue;
                }else if(prev[k]>0 && cur[k]>0){
                    prev[k]=Math.min(prev[k],cur[k]);
                }
                else{
                    prev[k]=0;
                }
            }
        }
        List<String> ans=new ArrayList<>();
        for(int i=0;i<26;i++){
            if(prev[i]==0)
                continue;
            for(int j=0;j<prev[i];j++){
                ans.add(String.valueOf((char)('a'+i)));
            }
        }
        return ans;
    }
}