class Solution:
    def addDigits(self, num: int) -> int:
        ans=num
        while ans>9:
            temp=0
            while ans>0:
                rem=ans%10
                temp+=rem
                ans=ans//10
            ans=temp
        return ans
        