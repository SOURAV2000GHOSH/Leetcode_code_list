class Solution:
    def removeElement(self, n: List[int], val: int) -> int:
        if len(n)==1 and n[0]==val:
            return 0
        index=0
        for i in range(len(n)):
            if n[i] != val:
                n[index]=n[i]
                index += 1
        return index
        
#         l=1
#         r=1
#         while r<len(n):
#             if n[l]==val and n[r]==val:
                
#                 pass
#             if n[l]==val and n[r] != val:
#                 n[l]=n[r]
#                 l+=1
#                 r+=1
#             if n[l] != val and n[r]==val:
#                 n[r]=n[l]
#                 l+=1
#                 r+=1
                