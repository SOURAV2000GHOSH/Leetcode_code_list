class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int a=x;
        int temp=0;
        int rem;
        while(a>0){
            rem=a%10;
            temp=(temp*10)+rem;
            a=a/10;  
        }
        if(temp==x){
            return true;
        }
        return false;
    }
}