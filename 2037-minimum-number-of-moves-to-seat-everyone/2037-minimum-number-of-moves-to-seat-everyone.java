class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        int []seat=new int[101];
        int []student=new int[101];
        for(int n:seats){
            seat[n]+=1;
        }
        for(int n:students){
            student[n]+=1;
        }
        int i=0,j=0,move=0;
        while(i<101 && j<101){
            if(seat[i]>0 && student[j]>0){
                move+=(Math.abs(i-j));
                seat[i]--;
                student[j]--;
                if(seat[i]==0){
                    i++;
                }
                if(student[j]==0){
                    j++;
                }
            }else if(seat[i]>0){
                j++;
            }else if(student[j]>0){
                i++;
            }else{
                i++;
                j++;
            }
        }
        return move;
    }
}