class Node{
    public char c;
    public int ind;
    public Node(char c,int ind){
        this.c=c;
        this.ind=ind;
    }
}

class Solution {
    public String clearStars(String s) {
        char[] arr=s.toCharArray();
        Queue<Node> minHeap= new PriorityQueue<>((a,b)->{
            if(a.c>b.c){
                return 1;
            }else if(a.c<b.c){
                return -1;
            }else{
                if(a.ind>b.ind){
                    return -1;
                }
                return 1;
            }
        });
        for(int i=0;i<arr.length;i++){
            if(arr[i]=='*'){
                Node peek=minHeap.poll();
                arr[peek.ind]='*';
            }else{
                minHeap.add(new Node(arr[i],i));
            }
        }
        StringBuilder ans= new StringBuilder();
        for(int i=0;i<arr.length;i++){
            if(arr[i]!='*'){
                ans.append(String.valueOf(arr[i]));
            }
        }
        return ans.toString();
    }
}