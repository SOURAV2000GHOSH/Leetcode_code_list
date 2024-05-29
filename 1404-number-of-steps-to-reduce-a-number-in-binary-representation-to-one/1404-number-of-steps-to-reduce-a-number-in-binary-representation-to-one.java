class Solution {
    public String change(String str){
        String s=new String();
        int i=str.length()-1;
        while(i>=0){
            char temp=str.charAt(i);
            if(temp=='1'){
                s="0"+s;
            }else{
                s="1"+s;
                break;
            }
            i--;
        }
        if(i>=0)
            s=str.substring(0,i)+s;
        if(i==-1){
            s="1"+s;
        }
        return s;
    }
    public int numSteps(String s) {
        int step=0;
        while(s.length()!=1){
            if(s.charAt(s.length()-1)=='1'){
                s=change(s);
            }else{
                s=s.substring(0,s.length()-1);
            }
            step++;
        }
        return step;
        
    }
}