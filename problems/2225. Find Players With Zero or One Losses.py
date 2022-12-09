# link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loseOne = set()
        loseMultiple = set()

        for winner, loser in matches:
            if winner not in loseOne and winner not in loseMultiple:
                winners.add(winner)
            if loser in winners:
                winners.remove(loser)
            if loser not in loseMultiple and loser not in loseOne:
                loseOne.add(loser)
            elif loser in loseOne:
                loseOne.remove(loser)
                loseMultiple.add(loser)

        winners = sorted(list(winners))
        loseOne = sorted(list(loseOne))
        return [winners, loseOne]
