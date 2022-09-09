# link: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        aCount = bCount = curCount = 0
        isA = True
        
        for c in colors:
            if (isA and c == 'A') or (not isA and c == 'B'):
                curCount += 1
            else:
                if isA:
                    aCount += max(0, curCount-2)
                else:
                    bCount += max(0, curCount-2)
                isA = not isA
                curCount = 1
                
        if isA:
            aCount += max(0, curCount-2)
        else:
            bCount += max(0, curCount-2)
            
        return aCount > bCount