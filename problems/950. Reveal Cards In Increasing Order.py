# link: https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        q = deque(range(n))
        deck.sort()
        result = [0] * n        
        for card in deck:
            i = q.popleft() # the index of the drawn card
            result[i] = card
            if q:
                q.append(q.popleft())
        
        return result