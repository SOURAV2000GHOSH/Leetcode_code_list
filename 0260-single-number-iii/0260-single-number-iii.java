class Solution {
    public int[] singleNumber(int[] nums) {
        int temp=0;
        for(int n:nums){
            temp=temp^n;
        }
        int bit=1;
        while((temp&bit)==0){
            bit=(bit<<1);
        }
        int temp1=0,temp2=0;
        for(int n:nums){
            if((n&bit)==0){
                temp1=temp1^n;
            }else{
                temp2=temp2^n;
            }
        }
        int ans[]={temp1,temp2};
        return ans;
    }
}