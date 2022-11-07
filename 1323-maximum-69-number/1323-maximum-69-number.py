class Solution:
    def maximum69Number (self, num: int) -> int:
        temp=str(num)
        for i in range(len(temp)):
            if temp[i]=='6':
                temp_num=temp[:i]+'9'+temp[i+1:]
                return int(temp_num)
        return num