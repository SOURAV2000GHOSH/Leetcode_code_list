class Solution:
    def intToRoman(self, num: int) -> str:
        cheak={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        ans=[]
        for x in cheak.keys():
            count=num//x
            temp=[count]
            while temp[0]>0:
                ans.append(cheak[x])
                temp[0]-=1
            num-=x*count
        return "".join(ans)
        