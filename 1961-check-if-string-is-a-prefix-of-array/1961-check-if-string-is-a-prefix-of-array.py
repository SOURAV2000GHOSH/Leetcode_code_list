class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l=0
        wordNumber=0
        length=len(s)
        while l<length:
            for x in words[wordNumber]:
                if l==length or s[l]!=x :
                    return False
                l+=1
            wordNumber += 1
            if wordNumber>(len(words)-1):
                break
        if l<length:
            return False
        return True
        