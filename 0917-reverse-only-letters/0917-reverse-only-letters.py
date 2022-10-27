class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        cheak=set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        ans=list(s)
        start=0
        end=len(s)-1
        while start<end:
            if ans[start] in cheak and ans[end] in cheak:
                ans[start],ans[end]=ans[end],ans[start]
                start+=1
                end-=1
            elif ans[start] not in cheak and ans[end] in cheak:
                start+=1
            elif ans[start] in cheak and ans[end] not in cheak:
                end-=1
            else:
                start+=1
                end-=1
        return "".join(ans)