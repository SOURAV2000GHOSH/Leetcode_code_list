class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        k=0
        for x in operations:
            if x=="++X" or x=="X++":
                k += 1
            if x=="--X" or x=="X--":
                k -= 1
        return k
        