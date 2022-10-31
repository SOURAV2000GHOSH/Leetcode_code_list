class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def search(key_list,prev):
            start,end=0,len(key_list)
            while start<end:
                mid=(start+end)//2
                if prev<key_list[mid]:
                    end=mid
                else:
                    start=mid+1
            return start
                
        cheak=defaultdict(list)
        count=0
        for indx,el in enumerate(s):
            cheak[el].append(indx)
                 
        for word in words:
            prev=-1
            found=True
            for char in word:
                temp=search(cheak[char],prev)
                if temp==len(cheak[char]):
                    found=False
                    break
                else:
                    prev=cheak[char][temp]
            if found:
                count+=1
        return count