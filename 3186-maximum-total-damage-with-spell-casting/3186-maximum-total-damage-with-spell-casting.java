class Solution {
    public long function(int ind,HashMap<Integer,Integer> check,int []power,long []dp){
        if(ind>=power.length)
            return 0;
        if(dp[ind]!=-1){
            return dp[ind];
        }
        //finding next Index which is is not equal to power[i] + 1 or power[i] + 2
        int nexInd=ind;
        while(nexInd<power.length && power[nexInd]-power[ind]<=2){
            nexInd++;
        }
        /*at the time of taking we just multiply that 
        element with it's number of frequency */
        long  take=(1l*check.get(power[ind])*power[ind])+function(nexInd,check,power,dp);
        
        long notTake=function(ind+1,check,power,dp);
        return dp[ind]=Math.max(take,notTake);
    }
    public long maximumTotalDamage(int[] power) {
        //store frequency of elements
        HashMap<Integer,Integer> mp=new HashMap<>();
        for(int x:power){
            if(mp.containsKey(x)){
                mp.put(x,mp.get(x)+1);
            }else{
                mp.put(x,1);
            }
        }
        //storing as distinct element that will send for calculation
        int []temp=new int[mp.size()];
        int i=0;
        for(int x:mp.keySet()){
            temp[i]=x;
            i++;
        }
        //sending as sorted format only checking for power[i] + 1, or power[i] + 2
        Arrays.sort(temp);
        long []dp=new long[power.length+1];
        Arrays.fill(dp,(long)-1);
        
        return function(0,mp,temp,dp);
    }
}