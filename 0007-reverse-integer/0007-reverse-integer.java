class Solution {
    public int reverse(int x) { 
        int negative= x<0?-1:1;
        long num=0;
        x=Math.abs(x);
        while(x>0){
            num=(num*10)+(x%10);
            x=(int)x/10;
        }
        if(num>=-(Math.pow(2,31)) && num<=((Math.pow(2,31)-1)))
            return (int)num*negative;
        return 0;
        
    }
}