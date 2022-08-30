class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            half_ans=calculate(x,n//2)
            if n%2 == 1:
                return half_ans*half_ans*x
            return half_ans*half_ans
        if n==0:
            return 1
        if x==0:
            return 0
        isxneg,isnneg=x<0,n<0
        absx=abs(x)
        absn=abs(n)
        ans=calculate(absx,absn)
        if isxneg and n%2==1:
            ans=-ans
        if isnneg:
            ans=1/ans
        
        return ans