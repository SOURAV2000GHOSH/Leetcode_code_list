class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
//         int n=nums.length;
//         HashMap<Long,Integer> []mp= new HashMap[n];
//         int ans=0;
//         for(int i=0;i<n;i++){
//             mp[i]=new HashMap<Long,Integer>();
//             for(int j=0;j<i;j++){
//                 Long diff=(Long)nums[i]-nums[j];
//                 if(mp[j].containsKey(dif)){
                    
//                 }else{
                    
//                 }
//             }
//         }
        int n = nums.length;
        int result = 0;
        Map<Long, Integer>[] mp = new HashMap[n];

        for (int i = 0; i < n; i++) {
            mp[i] = new HashMap<>();
            for (int j = 0; j < i; j++) {
                long diff = (long) nums[i] - nums[j];
                int count_at_j = mp[j].getOrDefault(diff, 0);

                result += count_at_j;
                
                // Increment the count at index i
                mp[i].put(diff, mp[i].getOrDefault(diff, 0) + count_at_j + 1);
            }
        }
        return result;
    }
}