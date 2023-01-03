class Solution {
    public int minDeletionSize(String[] str) {
        int m=str.length;
        int n=str[0].length();
        int count=0;
        for(int i=0;i<n;i++){//column
            for(int j=1;j<m;j++){//row
                if((int)str[j].charAt(i)<(int)str[j-1].charAt(i)){
                    count++;
                    break;
                }
            }
        }
        return count;
        
    }
}