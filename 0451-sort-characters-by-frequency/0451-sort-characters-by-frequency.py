class Solution:
    def frequencySort(self, s: str) -> str:
        freq=dict()
        for x in s:
            if x not in freq:
                freq[x]=1
            else:
                freq[x]+=1
        cheak=[]
        for x in freq.keys():
            cheak.append([freq[x],x])
        cheak.sort(reverse=True,key=lambda e:e[0])
        print(cheak)
        ans=[]
        for x,y in cheak:
            for x in range(x):
                ans.append(y)
        return "".join(ans)