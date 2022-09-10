class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        cheak=set([n])
        temp=n
        while True:
            tmp_sum=0
            while temp>0:
                rem=temp%10
                tmp_sum += (rem**2)
                temp=temp//10
            temp=tmp_sum
            if temp==1:
                return True
            if temp in cheak:
                return False
            else:
                cheak.add(temp)
                
                
            
            
            
            
            
        