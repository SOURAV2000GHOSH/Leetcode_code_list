class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        if l==0:
            return False
        cheak=set('aeiouAEIOU')
        count1=0
        count2=0
        indx=0
        while indx<l//2:
            if s[indx] in cheak:
                count1 += 1
            indx+=1
        while indx<l:
            if s[indx] in cheak:
                count2 += 1
            indx+=1
        if count1==count2:
            return True
        return False