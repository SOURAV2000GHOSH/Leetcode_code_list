class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        
        cheak=dict()
        for x in deck:
            if x in cheak:
                cheak[x]+=1
                continue
            cheak[x]=1
        ans=0
        print(cheak)
        for x in cheak.keys():
            ans=gcd(max(ans,cheak[x]),min(ans,cheak[x]))
        if ans>1:
            return True
        return False
            