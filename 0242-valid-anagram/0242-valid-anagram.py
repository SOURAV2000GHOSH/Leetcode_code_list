class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        store1=dict()
        store2=dict()
        for x in range(len(s)):
            store1[s[x]]=1 if s[x] not in store1 else store1[s[x]]+1
            store2[t[x]]=1 if t[x] not in store2 else store2[t[x]]+1    
        for x in store1.keys():
            if x not in store2 or store1[x]!=store2[x]:
                return False
        for x in store2.keys():
            if x not in store1 or store1[x]!=store2[x]:
                return False
        return True