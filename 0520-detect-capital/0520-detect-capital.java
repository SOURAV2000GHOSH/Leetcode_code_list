class Solution {
    public boolean detectCapitalUse(String word) {
        int capitalCount=0;
        int smallCount=0;
        int l=word.length();
        for(int i=0;i<l;i++){
            int letter_unicode=(int)word.charAt(i);
            if(65 <=letter_unicode && letter_unicode<=90)
                capitalCount+=1;
            else
                smallCount+=1;
        }
        if(capitalCount == l || smallCount==l)
            return true;
        if(65 <=(int)word.charAt(0) && (int)word.charAt(0)<=90 && smallCount==(l-1))
            return true;
        return false;
        
    }
}