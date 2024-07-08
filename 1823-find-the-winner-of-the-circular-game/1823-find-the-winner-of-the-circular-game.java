class Solution {
    public int findTheWinner(int n, int k) {
        Queue<Integer> arr=new LinkedList<>();
        for(int i=1;i<=n;i++){
            arr.add(i);
        }
        int temp=1;
        while(arr.size()>1){
            int first=arr.poll();
            if(temp==k){
                temp=1;
            }else{
                arr.add(first);
                temp++;
            }
        }
        return arr.peek();
    }
}