class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def findEquationValue(p1,p2,p3):
            x1=p1[0]
            x2=p2[0]
            x3=p3[0]
            y1=p1[1]
            y2=p2[1]
            y3=p3[1]
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
        
        if len(trees)<3:
            return trees
        trees.sort()
        lower=[]
        upper=[]
        for x in trees:
            l=len(lower)
            u=len(upper)
            while l>=2 and findEquationValue(lower[l-2],lower[l-1],x)<0:
                l-=1
                lower.pop()
            while u>=2 and findEquationValue(upper[u-2],upper[u-1],x)>0:
                u-=1
                upper.pop()
            lower.append(x)
            upper.append(x)
        
        ans=set()
        for i in lower:
            ans.add((i[0],i[1]))
        for i in upper:
            ans.add((i[0],i[1]))
        temp=[]
        for x in ans:
            temp.append([x[0],x[1]])
        return temp
            
        
        
        