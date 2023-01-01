class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        check1=dict()
        check2=dict()
        s1=s.split(" ")
        if len(pattern) != len(s1):
            return False
        for i in range(len(pattern)):
            if s1[i] in check1:
                if check1[s1[i]] !=pattern[i]:
                    return False
            elif pattern[i] in check2:
                if check2[pattern[i]] !=s1[i]:
                    return False
            else:
                check1[s1[i]]=pattern[i]
                check2[pattern[i]]=s1[i]
            
        return True