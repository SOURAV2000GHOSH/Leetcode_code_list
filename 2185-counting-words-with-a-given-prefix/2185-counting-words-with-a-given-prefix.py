class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        l=len(pref)
        for word in words:
            i=0
            while i<l and i<len(word):
                if word[i] != pref[i]:
                    break
                i+=1
            if i==l:
                count += 1
                
        return count
        