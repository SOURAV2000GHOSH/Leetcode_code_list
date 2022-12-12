class Solution:
    def climbStairs(self, n: int) -> int:
        #this is use for memoization
        check=[0]*46
        
        def solve(rem,check):
            if rem<0:
                return 0
            if rem==0:
                return 1
            if check[rem] !=0:
                return check[rem]
            total=solve(rem-1,check)+solve(rem-2,check)
            #using memoization
            check[rem]=total
            return total
        
        return solve(n,check)
        