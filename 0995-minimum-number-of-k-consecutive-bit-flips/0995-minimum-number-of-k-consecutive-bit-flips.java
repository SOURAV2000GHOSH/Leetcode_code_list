class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int curFlip=0,totalFlip=0,n=nums.length;
        boolean isFlip[]=new boolean[n];
        for(int i=0;i<n;i++){
            if(i>=k && isFlip[i-k]){
                curFlip--;
            }
            if(curFlip%2 == nums[i]){
                if(i+k>n)
                    return -1;
                isFlip[i]=true;
                curFlip++;
                totalFlip++;
            }
        }
        
        return totalFlip;
        
    }
}