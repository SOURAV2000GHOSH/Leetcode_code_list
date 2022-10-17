class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordcount=1
        isprefix=True
        l=0
        start=0
        while l<len(sentence):
            #cheak all searchWord character have
            if start==len(searchWord):
                break
            if sentence[l]!=searchWord[start]:
                start=0
                isprefix=False
            if isprefix and sentence[l]==searchWord[start]:
                start+=1
            if sentence[l]==" ":
                start=0
                isprefix=True
                wordcount += 1
            l+=1
        if start==0:
            return -1
        return wordcount
        