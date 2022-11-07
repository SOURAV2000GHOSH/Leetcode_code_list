class Solution:
    # def makeNum(arr):
    #     num=0
    #     for x in arr:
    #         num=(num*10)+x
    #     return num
    def maximum69Number (self, num: int) -> int:
        max_num=[num]
        temp=str(num)
        for i in range(len(temp)):
            if temp[i]=='6':
                temp_num=temp[:i]+'9'+temp[i+1:]
                if int(temp_num)>max_num[0]:
                    max_num[0]=int(temp_num)
                    break
        return max_num[0]
        
            
            
        