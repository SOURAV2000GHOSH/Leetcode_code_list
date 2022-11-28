class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans0=[]
        check0=dict()
        ans1=[]
        check1=dict()
        for x,y in matches:
            if y in check0:
                check0.pop(y)
                check1[y]=1
            elif y in check1:
                check1[y]+=1
            else:
                check1[y]=1
            if x in check1:
                continue
            else:
                check0[x]=1
        for x in check0.keys():
            ans0.append(x)
        ans0.sort()
        for x in check1.keys():
            if check1[x]==1:
                ans1.append(x)
        ans1.sort()
        return [ans0,ans1]
                
                    
        