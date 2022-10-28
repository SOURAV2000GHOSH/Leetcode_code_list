class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cheak=dict()
        for x in strs:
            temp="".join(sorted(x))
            if temp not in cheak:
                cheak[temp]=[x]
            else:
                cheak[temp].append(x)
        return cheak.values()
        