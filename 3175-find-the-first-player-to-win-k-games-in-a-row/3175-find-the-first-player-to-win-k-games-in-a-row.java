class Node{
    int no,skill;
    public Node(int no,int skill){
        this.no=no;
        this.skill=skill;
    }
}
class Solution {
    public int findWinningPlayer(int[] skills, int k) {
        int cur=-1,count=0,n=skills.length;
        if(k>=n){
            int tempMax=-1,ind=-1;
            for(int i=0;i<n;i++){
                if(tempMax<skills[i]){
                    ind=i;
                    tempMax=skills[i];
                }
            }
            return ind;
        }
        LinkedList<Node> l=new LinkedList<>();
        for(int i=0;i<n;i++){
            l.add(new Node(i,skills[i]));
        }
        while(true){
            Node first=l.poll();
            Node second=l.poll();
            if(first.skill>second.skill){
                l.add(0,first);
                l.add(second);
                if(cur==first.no){
                    count++;
                }else{
                    cur=first.no;
                    count=1;
                }
            }else{
                l.add(0,second);
                l.add(first);
                if(cur==second.no){
                    count++;
                }else{
                    cur=second.no;
                    count=1;
                }
            }
            if(count==k)
                break;
        }
        return cur;
    }
}