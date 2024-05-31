class Solution {
    public int[] singleNumber(int[] nums) {
        //getting XOR value of two unique values
        int temp=0;
        for(int n:nums){
            temp=temp^n;
        }
        
        // getting the bit that will differenciate between that two numbers 
        int bit=1;
        while((temp&bit)==0){
            bit=(bit<<1);
        }
        
        /*based on that bits dividing whole array into two parts 
        and get two unique value*/
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