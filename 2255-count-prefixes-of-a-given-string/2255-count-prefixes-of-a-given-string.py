class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for x in words:
            if s.startswith(x):
                count += 1
        return count
                