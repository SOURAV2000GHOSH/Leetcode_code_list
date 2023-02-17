class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        store=["0","1","2","3","4","5","6","7","8","9"]
        check={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        before=0
        l1=len(num1)
        l2=len(num2)
        ans=[""]*(max(l1,l2)+1)
        l1-=1
        l2-=1
        n=len(ans)-1
        if l1>l2:
            while l2>-1 and l1>-1:
                temp=check[num1[l1]]+check[num2[l2]]+before
                ans[n]=store[temp%10]
                before=temp//10
                n-=1
                l1-=1
                l2-=1
            while l1>-1:
                temp=check[num1[l1]]+before
                ans[n]=store[temp%10]
                before=temp//10
                n-=1
                l1-=1
        else:
            while l1>-1 and l2>-1:
                temp=check[num1[l1]]+check[num2[l2]]+before
                ans[n]=store[temp%10]
                before=temp//10
                n-=1
                l1-=1
                l2-=1
            while l2>-1:
                temp=check[num2[l2]]+before
                ans[n]=store[temp%10]
                before=temp//10
                n-=1
                l2-=1
        if before>0:
            ans[n]=store[before]
        
        return "".join(ans)
            
            
                