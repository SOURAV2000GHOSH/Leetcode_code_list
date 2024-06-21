class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int ans=0;
        int n=customers.length;
        for(int i=0;i<n;i++){
            int unsatisfied=0;
            for(int j=i;j<n && j<i+minutes;j++){
                if(grumpy[j]==0){
                   continue;
                }else{
                    unsatisfied+=customers[j];
                }
            }
            ans=Math.max(unsatisfied,ans);
        }
        for(int i=0;i<n;i++){
            if(grumpy[i]==0){
                ans+=customers[i];
            }
        }
        return ans;
    }
}