class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m,n=len(s1),len(s2)
        t=[[0 for i in range((n+1))] for i in range((m+1))]
        for i in range(1,(m+1)):
            for j in range(1,(n+1)):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i][j-1],t[i-1][j])
        return t[-1][-1]        