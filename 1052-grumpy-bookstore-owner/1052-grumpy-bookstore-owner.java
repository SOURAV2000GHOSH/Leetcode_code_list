class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int n=customers.length;
        int start=0;
        int maxUnsatisfied=0;
        int curUnsatisfied=0;
        for(int i=0;i<minutes;i++){
            if(grumpy[i]==1){
                curUnsatisfied+=customers[i];
            }
        }
        maxUnsatisfied=curUnsatisfied;
        int i=0,j=minutes;
        while(j<n){
            if(grumpy[j]==1){
                curUnsatisfied+=customers[j];
            }
            if(grumpy[i]==1){
                curUnsatisfied-=customers[i];
            }
            maxUnsatisfied = Math.max(maxUnsatisfied,curUnsatisfied);
            i++;
            j++;
        }
        int ans=maxUnsatisfied;
        for(int k=0;k<n;k++){
            if(grumpy[k]==0){
                ans+=customers[k];
            }
        }
        return ans;
    }
}