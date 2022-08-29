class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=set("abcdefghijklmnopqrstuvwxyz0123456789")
        left=0
        right=len(s)-1
        while left<right:
            if s[left] not in a:
                left +=1
                continue
            if s[right] not in a:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True