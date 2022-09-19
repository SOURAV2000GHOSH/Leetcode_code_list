class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        temp={}
        for x in s1.split(" "):
            temp[x]=temp[x]+1 if x in temp else 1
        for x in s2.split(" "):
            temp[x]=temp[x]+1 if x in temp else 1
        for x in temp.keys():
            if temp[x]==1:
                ans.append(x)
        return ans
        
        
        