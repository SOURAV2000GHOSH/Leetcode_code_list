class Solution:
    def calculate(self, s: str) -> int:
        number_list={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        sign_cheak={'+':1,"-":-1}
        number=0
        result=0
        sign=1
        stack=[]
        l=0
        length=len(s)
        while l<length:
            x=s[l]
            if x==" ":
                l+=1
                continue
            else:
                if x=="(":
                    stack.append([result,sign])
                    result=0
                    number=0
                    sign=1
                if x==")":
                    result+=(number*sign)
                    temp=stack.pop()
                    result=temp[1]*result
                    result+=temp[0]
                    number=0
                    sign=1
                if x in number_list:
                    number=(number*10)+number_list[x]                    
                #x should be sign
                if x in sign_cheak:
                    result += (number*sign)
                    sign=sign_cheak[x]
                    number=0
                l+=1
        result += (number*sign)
        return result