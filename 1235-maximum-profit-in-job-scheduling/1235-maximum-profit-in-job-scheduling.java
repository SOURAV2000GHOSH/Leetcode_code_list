import java.util.*;
class Sortbyroll implements Comparator<ArrayList<Integer>> 
{   @Override
    public int compare(ArrayList<Integer> a, ArrayList<Integer> b) 
    { 
        if(a.get(0)==b.get(0)){
            return 0;
        }
        else if(a.get(0)>b.get(0)){
            return 1;
        }else{
            return -1;
        }
    } 
} 
class Solution {
    public static int nextIndex(ArrayList<ArrayList<Integer>> arr,int l,int r,int target){
        int result=-1;
        while(l<=r){
            int mid=l-(l-r)/2;
            if(arr.get(mid).get(0)>=target){
                result=mid;
                r=mid-1;
            }else{
                l=mid+1;
            }
        }
        return result;
    }
    public static int solve(int ind,int n,ArrayList<ArrayList<Integer>> arr,Integer []dp){
        if(ind==n || ind==-1){
            return 0;
        }
        if(dp[ind]!=null){
            return dp[ind];
        }
        int nexInd=Solution.nextIndex(arr,ind+1,n-1,arr.get(ind).get(1));
        int take=arr.get(ind).get(2)+Solution.solve(nexInd,n,arr,dp);
        int notTake=Solution.solve(ind+1,n,arr,dp);
        dp[ind]=Math.max(take,notTake);
        return dp[ind];
    }
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n=startTime.length;
        Integer []dp=new Integer[n];
        ArrayList<ArrayList<Integer>> store = new ArrayList<>();
        for(int i=0;i<n;i++){
            ArrayList<Integer> temp=new ArrayList<>();
            temp.add(startTime[i]);
            temp.add(endTime[i]);
            temp.add(profit[i]);
            store.add(temp);
        }
        Collections.sort(store,new Sortbyroll());
        return Solution.solve(0,n,store,dp);
        
    }
}