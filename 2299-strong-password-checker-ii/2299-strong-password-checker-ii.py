class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        lower=set('abcdefghijklmnopqrstuvwxyz')
        upper=set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        digit=set('1234567890')
        sp_char=set("!@#$%^&*()-+")
        count_lower=count_upper=count_sp=count_digit=0
        for x in range(len(password)):
            if x>0 and password[x]==password[x-1]:
                return False
            if password[x] in upper:
                count_upper+=1
            elif password[x] in lower:
                count_lower +=1
            elif password[x] in digit:
                count_digit += 1
            elif password[x] in sp_char:
                count_sp += 1
        if count_lower>=1 and count_upper>=1 and count_digit>=1 and count_sp>=1:
            return True
        return False
            
        