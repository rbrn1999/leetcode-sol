from functools import cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def first(intTuple, total) -> bool:
            if len(intTuple)==0:
                return False
            if intTuple[0] >= total:
                return True
            
            permutations = []
            for i in range(len(intTuple)):
                curTuple = intTuple[:i] + intTuple[i+1:]
                curTotal = total-intTuple[i]
                permutations.append((curTuple, curTotal))
            return any(second(a, t) for a, t in permutations)
        
        @cache
        def second(intTuple, total) -> bool:
            if len(intTuple)==0 or intTuple[0] >= total:
                return False
            
            permutations = []
            for i in range(len(intTuple)):
                curTuple = intTuple[:i] + intTuple[i+1:]
                curTotal = total-intTuple[i]
                permutations.append((curTuple, curTotal))
            return all(first(a, t) for a, t in permutations)
        
        return first(tuple(range(maxChoosableInteger, 0, -1)), desiredTotal)

print(Solution().canIWin(20, 152))


# alternative solution
# reference: https://leetcode.com/problems/can-i-win/discuss/159797
'''
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def helper(choices, remainder):
            if choices[0] >= remainder:
                return True
            
            # current player's choices:
            for i in range(len(choices)):
                if not helper(choices[:i]+choices[i+1:], remainder-choices[i]):
                    # the next player can't force a win,
                    # so the current player can (because there's no draw)
                    return True
                
            # the current player can't win with any choices
            return False
        
        
        if maxChoosableInteger*(maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        elif maxChoosableInteger*(maxChoosableInteger + 1) // 2 == desiredTotal:
            return (maxChoosableInteger % 2) == 1 # odd number of turns
        else:
            return helper(tuple(range(maxChoosableInteger, 0, -1)), desiredTotal)
'''