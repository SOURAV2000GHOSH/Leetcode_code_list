class Solution {
    public boolean judgeSquareSum(int c) {
        long start=0,end=(long)Math.sqrt(c);
        while(start<=end){
            long sum=(start*start)+(end*end);
            if(sum==c)
                return true;
            if(sum<c)
                start++;
            else
                end--;
        }
        return false;
    }
}