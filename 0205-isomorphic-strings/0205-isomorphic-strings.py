class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        cheak=dict()
        for x in range(len(s)):
            if s[x] in cheak:
                if cheak[s[x]] != t[x]:
                    return False
            else:
                cheak[s[x]]=t[x]
        return True
        