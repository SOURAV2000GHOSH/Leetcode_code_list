class Solution:
    def numberOfSteps(self, num: int) -> int:
        step=0
        while num>0:
            step+=1
            if num%2==1:
                num-=1
            else:
                num=num//2
        return step
        