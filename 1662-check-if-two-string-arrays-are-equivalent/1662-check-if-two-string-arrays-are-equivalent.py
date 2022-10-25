class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        len1=len(word1)
        len2=len(word2)
        l1=0
        l2=0
        temp1=0
        temp2=0
        while l1<len1 and l2<len2:
            temp_len1 = len(word1[l1])
            temp_len2 = len(word2[l2])
            while temp1<temp_len1 and temp2<temp_len2:
                if word1[l1][temp1] != word2[l2][temp2]:
                    return False
                temp1 += 1
                temp2 += 1
            if temp1 == temp_len1:
                temp1 = 0
                l1 += 1
            if temp2 == temp_len2:
                temp2 = 0
                l2 += 1
        if l1<len1 or l2<len2:
            return False
        return True