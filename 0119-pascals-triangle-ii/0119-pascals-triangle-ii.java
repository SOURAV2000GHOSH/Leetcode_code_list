class Solution {
    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> prev=new ArrayList<>();
        ArrayList<Integer> cur;
        for(int i=0;i<=rowIndex;i++){
            int n=prev.size();
            cur=new ArrayList(n+1);
            for(int j=0;j<=n;j++){
                if(j==0 || j==n){
                    cur.add(1);
                }else{
                    cur.add(prev.get(j)+prev.get(j-1));
                }
            }
            prev=cur;
        }
        return prev;
    }
}