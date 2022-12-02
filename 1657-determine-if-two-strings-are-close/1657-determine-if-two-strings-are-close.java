class Solution {
    public boolean closeStrings(String word1, String word2) {
        //two words must be of same length in order to be close
        if(word1.length()!=word2.length()){
            return false;
        }
        // next we check if count of distinct char's order is same
        // for that we record freq of both words and sort then to check the above condition
        int[] freq1=new int[26];
        for(char i:word1.toCharArray()){
            freq1[i-'a']++;
        }
        int[] freq2=new int[26];
        for(char i:word2.toCharArray()){
            if(freq1[i-'a']==0){   // we do this because both the words must contain same distinct char's
                return false;
            }
            freq2[i-'a']++;
        }
        Arrays.sort(freq1);
        Arrays.sort(freq2);
        String first=Arrays.toString(freq1);
        String second=Arrays.toString(freq2);
        return first.equals(second);
    }
}
