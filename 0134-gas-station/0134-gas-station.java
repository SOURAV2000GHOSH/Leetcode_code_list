class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n=gas.length;
        int totalGas=Arrays.stream(gas).sum();
        int totalCost=Arrays.stream(cost).sum();
        //if cost of all station is greater than sum of gas then we can cont complete all station that's why we return -1;
        // for(int i=0;i<n;i++){
        //     totalGas+=gas[i];
        //     totalCost+=cost[i];
        // }
        if(totalCost>totalGas){
            return -1;
        }
        //if get 0 or positive total in any index then we get answer;
        int result=0;
        int total=0;
        for(int i=0;i<n;i++){
            total=total+gas[i]-cost[i];
                if(total<0){
                    total=0;
                    result=i+1;
                }
        }
        return result;
    }
}