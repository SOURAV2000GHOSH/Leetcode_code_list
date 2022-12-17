class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x=="+" or x=="-" or x=="*" or x=="/":
                temp=0
                b=stack.pop(-1)
                a=stack.pop(-1)
                if x=="*":
                    temp=b*a
                elif x=="/":
                    temp=int(a/b)
                elif x=="+":
                    temp=a+b
                elif x=="-":
                    temp=a-b
                stack.append(temp)
                print(temp)
                continue
                
            number=0
            numbersign=+1
            length=len(x)
            l=0
            if x[0]=="-":
                numbersign=-1
                l=1
            
            while l<length:
                number=(number*10)+int(x[l])
                l+=1
            temp_num=number*numbersign
            stack.append(temp_num)
        return stack[0]
        