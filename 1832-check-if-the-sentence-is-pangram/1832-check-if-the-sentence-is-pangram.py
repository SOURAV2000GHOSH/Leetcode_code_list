class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cheak=set(sentence)
        myWord="abcdefghijklmnopqrstuvwxyz"
        for x in myWord:
            if x not in cheak:
                return False
        return True
        