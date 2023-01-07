brute force
​
```
class Solution {
public int canCompleteCircuit(int[] gas, int[] cost) {
int n=gas.length;
for(int i=0;i<n;i++){
int curVal=gas[i];
if(curVal<cost[i])
continue;
int j=(i+1)%n;
int beforeCostVal=cost[i];//store before cost value of j
while(j!=i){
curVal=curVal-beforeCostVal+gas[j];
beforeVal=cost[j];
if(curVal<cost[j])
break;
j=(j+1)%n;
}
if(j==i){
return i;
}
}
return -1;
}
}
```