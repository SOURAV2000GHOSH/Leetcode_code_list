class Solution {
    public int[] singleNumber(int[] nums) {
        if(nums.length==2){
            return nums;
        }
        Arrays.sort(nums);
        int temp=0;
        boolean getfirst=false;
        int ans[]={-1,-1};
        for(int i=0;i<nums.length;i++){
            int n=nums[i];
            if(n==0){
                if(i==nums.length-1 && nums[i]!=nums[i-1]){
                    if(getfirst){
                        ans[1]=n;
                    }else{
                        ans[0]=n;
                        getfirst=true;
                    }
                }else if(i==0 && nums[i]!=nums[i+1]){
                    if(getfirst){
                        ans[1]=n;
                    }else{
                        ans[0]=n;
                        getfirst=true;
                    }  
                }else if(i>0 && i< nums.length && nums[i]!=nums[i-1] && nums[i]!=nums[i+1]){
                    if(getfirst){
                        ans[1]=n;
                    }else{
                        ans[0]=n;
                        getfirst=true;
                    }
                    
                }
                continue;
            }
            if((temp^n)==0){
                temp=0;
                continue;
            }else{
                if(i==nums.length-1 || (i<nums.length-1 && nums[i]!=nums[i+1])){
                    if(getfirst){
                        ans[1]=n;
                    }else{
                        ans[0]=n;
                        getfirst=true;
                    }
                }
                temp=n;
            }
        }
        return ans;
        
    }
}