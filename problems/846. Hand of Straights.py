# link: https://leetcode.com/problems/hand-of-straights/

from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
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

# Sorting
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        num_count = Counter(hand)
        hand.sort()

        for card in hand:
            if num_count[card] == 0:
                continue

            for i in range(groupSize):
                if num_count[card + i] == 0:
                    return False

                num_count[card + i] -= 1

        return True

# Reverse Decrement

from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        card_count = Counter(hand)
        groups = 0

        for card in hand:
            start_card = card

            # find a starting point (no card on its left)
            while card_count[start_card - 1] > 0:
                start_card -= 1

            while start_card <= card:
                while card_count[start_card]:
                    # check group [start_card, start_card+groupSize]
                    for next_card in range(start_card, start_card + groupSize):
                        if card_count[next_card] == 0:
                            return False

                        card_count[next_card] -= 1

                start_card += 1

        return True
