class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        temp=[]
        for x in s:
            if x not in a:
                continue
            temp.append(x)
        left=0
        right=len(temp)-1
        while left<right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True