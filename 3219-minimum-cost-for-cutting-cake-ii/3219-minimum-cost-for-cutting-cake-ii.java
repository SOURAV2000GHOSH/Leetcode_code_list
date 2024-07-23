class Solution {
    public List<Integer> sort(int []temp){
        List<Integer> arr = new ArrayList<>();
        for(int n: temp){
            arr.add(n);
        }
        Collections.sort(arr,(a,b)->b-a);
        return arr;
    }
    public long minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        long ans=0;
        List<Integer> horizontalCutPrices = sort(horizontalCut);
        List<Integer> verticalCutPrices = sort(verticalCut);
        long horizontalPieces =1, verticalPieces = 1;
        int i=0,j=0;
        while(i<m-1 && j<n-1){
            int hCut=horizontalCutPrices.get(i);
            int vCut=verticalCutPrices.get(j);
            if(hCut>vCut){
                ans+=(verticalPieces*hCut);
                horizontalPieces++;
                i++;
            }else{
                ans+=(horizontalPieces*vCut);
                verticalPieces++;
                j++;
            }
        }
        while(i<m-1){
            ans+=(verticalPieces * horizontalCutPrices.get(i));
            horizontalPieces++;
            i++;
        }
        while(j<n-1){
            ans+=(horizontalPieces*verticalCutPrices.get(j));
            verticalPieces++;
            j++; 
        }
        
        return ans;
    }
}