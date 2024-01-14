class Solution {
    public boolean closeStrings(String word1, String word2) {
        int n1=word1.length(),n2=word2.length();
        if(n1!=n2){
            return false;
        }
        int []freq1=new int[26];
        for(int i=0;i<n1;i++){
            freq1[(int)(word1.charAt(i)-'a')]++;
        }
        int []freq2=new int[26];
        for(int i=0;i<n1;i++){
            if(freq1[(int)(word2.charAt(i)-'a')]==0)
                return false;
            freq2[(int)(word2.charAt(i)-'a')]++;
        }
        Arrays.sort(freq1);
        Arrays.sort(freq2);
        return Arrays.toString(freq1).equals(Arrays.toString(freq2));
    }
}