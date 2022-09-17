class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans=0
        temp={}
        temp1={}
        for x in words1:
            temp[x]=temp[x]+1 if x in temp else 1
        for x in words2:
            temp1[x]=temp1[x]+1 if x in temp1 else 1
        for x in temp.keys():
            if x in temp1 and temp[x]==1 and temp1[x]==1:
                ans+=1
        return ans
        