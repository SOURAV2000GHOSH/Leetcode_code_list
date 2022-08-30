class Solution:
    def validPalindrome(self, s: str) -> bool:        
        left=0
        right=len(s)-1
        while left<right:
            if s[left] != s[right]:
                l1,r1,l2,r2=left+1,right,left,right-1
                first_try,sec_try=True,True
                while l1<r1:
                    if s[l1]!=s[r1]:
                        first_try=False
                        break
                    l1 +=1
                    r1 -= 1
                while l2<r2:
                    if s[l2]!=s[r2]:
                        sec_try=False
                        break
                    l2 +=1
                    r2 -=1
                if first_try or sec_try:
                    return True
                else:
                    return False
            left +=1
            right -=1
        
        return True
         
    
        