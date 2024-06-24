class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int curFlip=0,totalFlip=0,n=nums.length;
        for(int i=0;i<n;i++){
            if(i>=k && nums[i-k]==-1){
                curFlip--;
            }
            if(curFlip%2 == nums[i]){
                if(i+k>n)
                    return -1;
                nums[i]=-1;
                curFlip++;
                totalFlip++;
            }
        }
        
        return totalFlip;
        
    }
}