class Solution {
    public List<Integer> sort(int []arr){
        List<Integer> list = new ArrayList<>();
        for(int n:arr){
            list.add(n);
        }
        Collections.sort(list,(a,b)->b-a);
        return list;
    }
    
    public int minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        int ans=0;
        int horizontalPices=1;
        int verticalPices=1;
        /* sorting in decrease order cause big values will use to reduce cost */
        List<Integer> hcut = sort(horizontalCut);
        List<Integer> vcut = sort(verticalCut);
        int i=0,j=0;
        while(i<m-1 && j<n-1){
            int hPrice=hcut.get(i);
            int vPrice=vcut.get(j);
            /* if we cut in horizontal pices then we horizontal 
            piece will be increase by 1 */
            if(hPrice>vPrice){
                ans+=(verticalPices*hPrice);
                horizontalPices++;
                i++;
            }
            /* if we cut in vertical pices then we vertical 
            piece will be increase by 1 */
            else{
                ans+=(horizontalPices*vPrice);
                verticalPices++;
                j++;
            }
        }
        while(i<m-1){
            int hPrice=hcut.get(i);
            ans+=(verticalPices*hPrice);
            horizontalPices++;
            i++;
        }
        while(j<n-1){
            int vPrice=vcut.get(j);
            ans+=(horizontalPices*vPrice);
            verticalPices++;
            j++;
        }
        return ans;
    }
}