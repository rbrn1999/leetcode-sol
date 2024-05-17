# link: https://leetcode.com/problems/24-game/

import math
import operator
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = [operator.add, operator.sub, operator.mul, operator.truediv]

        def dfs(cards: list[int]) -> bool:
            if len(cards) == 1:
                return math.isclose(cards[0], 24)

            for i in range(len(cards)-1):
                for j in range(i+1, len(cards)):
                    for op in ops:
                        if cards[j] != 0 or op != operator.truediv:
                            val = op(cards[i], cards[j])
                            new_cards = cards[:i] + cards[i+1:j] + cards[j+1:] + [val]
                            if dfs(new_cards):
                                return True

                        if op == operator.mul or op == operator.add:
                            continue

                        if cards[i] != 0 or op != operator.truediv:
                            val = op(cards[j], cards[i])
                            new_cards = cards[:i] + cards[i+1:j] + cards[j+1:] + [val]
                            if dfs(new_cards):
                                return True

            return False

        return dfs(cards)
