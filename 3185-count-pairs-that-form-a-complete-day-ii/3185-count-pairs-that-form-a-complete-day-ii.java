class Solution {
    public long countCompleteDayPairs(int[] hours) {
        long count=0;
        long []arr=new long[24];
        for(int hour:hours){
            int reminder=(24-(hour%24))%24;
            count+=arr[reminder];
            arr[hour%24]++;
        }
        return count;
    }
}