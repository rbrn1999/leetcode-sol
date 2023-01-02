# link: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        spaces = sorted([capacity[i] - rocks[i] for i in range(n)])

        for i in range(n):
            if additionalRocks < spaces[i]:
                return i
            additionalRocks -= spaces[i]

        return n
