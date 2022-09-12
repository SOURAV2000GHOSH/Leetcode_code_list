class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=0
        r=len(tokens)-1
        maxscore=0
        score=0
        while l<=r:
            if tokens[l]<=power:
                power-=tokens[l]
                score +=1
                l+=1
            elif score>0 :
                score -=1
                power+=tokens[r]
                r-=1
            else:
                return maxscore
            if maxscore<score:
                maxscore=score
        return maxscore