class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int consi=0;
        for(int n:arr){
            if(n%2==1){
                consi++;
            }else{
                consi=0;
            }
            if(consi==3)
                return true;
        }
        return false;
        
    }
}