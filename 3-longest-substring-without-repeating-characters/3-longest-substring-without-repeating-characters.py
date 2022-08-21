class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cheak=set()      
        l=0
        ans=0
        for r in range(len(s)):
                while s[r] in cheak:
                    cheak.remove(s[l])
                    l += 1
                ans=max(ans,(r-l+1))
                cheak.add(s[r])
        return ans
        
            