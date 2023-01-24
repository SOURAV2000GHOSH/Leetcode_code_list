class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=len(word1)+len(word2)
        store=[""]*(l)
        s1=0
        s2=0
        isWord1=True
        i=0
        while i<l:
            if s1==len(word1) or s2==len(word2):
                break
            if isWord1:
                store[i]=word1[s1]
                s1+=1
                isWord1=False
            else:
                store[i]=word2[s2]
                s2+=1
                isWord1=True
            i+=1
        if s1<len(word1):
            while i<l:
                store[i]=word1[s1]
                s1+=1
                i+=1
        elif s2<len(word2):
            while i<l:
                store[i]=word2[s2]
                s2+=1
                i+=1
            
        return "".join(store)
        