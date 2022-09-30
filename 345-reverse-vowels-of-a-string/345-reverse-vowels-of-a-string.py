class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set('aeiouAEIOU')
        temp=list(s)
        l=0
        r=len(temp)-1
        while l<r:
            if temp[l] in vowel and temp[r] in vowel:
                temp[l],temp[r]=temp[r],temp[l]
                l+=1
                r-=1
                continue
            if temp[l] not in vowel:
                l+=1
            if temp[r] not in vowel:
                r-=1
        
        return "".join(temp)