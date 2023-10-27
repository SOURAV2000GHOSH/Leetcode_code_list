class Solution {
    public String longestPalindrome(String str) {
        int ansLen=0,l=str.length();
        int start=-1,end=-1;
        
        for(int i=0;i<l;i++){
            //checking for odd length palindrom
            int s=i,e=i;
            while(s>=0 && e<l && str.charAt(s)==str.charAt(e)){
                if((e-s+1)>ansLen){
                    start=s;
                    end=e;
                    ansLen=(e-s+1);
                }
                s--;
                e++;
            }
            s=i;
            e=i+1;
            while(s>=0 && e<l && str.charAt(s)==str.charAt(e)){
                if((e-s+1)>ansLen){
                    ansLen=(e-s+1);
                    start=s;
                    end=e;
                }
                s--;
                e++;
            }
        }
        return str.substring(start,end+1);
        
    }
}