# link: https://leetcode.com/problems/hand-of-straights/

from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardCount = Counter(hand)
        heap = [card for card in cardCount]
        heapq.heapify(heap)
        while heap:
            card = heap[0]
            if cardCount.get(card, 0) == 0:
                heapq.heappop(heap)
                continue
            for _ in range(groupSize):
                if cardCount[card] == 0:
                    return False
                cardCount[card] -= 1
                card += 1

        return True
