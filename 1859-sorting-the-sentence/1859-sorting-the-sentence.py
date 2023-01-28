class Solution:
    def sortSentence(self, s: str) -> str:
        def myFunc(e):
            return int(e[len(e)-1])
        temp=s.split()
        temp.sort(key=myFunc)
        temp1=[]
        for i in temp:
            temp1.append(i[0:len(i)-1])
        return " ".join(temp1)
        