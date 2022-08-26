class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        ans=1
        for x in range(2,int(math.sqrt(num)+1)):
            if num%x==0:
                ans = ans +x+(num//x)
        if ans==num:
            return True
        return False
        