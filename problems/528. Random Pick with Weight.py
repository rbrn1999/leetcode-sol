# link: https://leetcode.com/problems/random-pick-with-weight/

import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        self.len = len(w)
        weightSum = sum(w)
        total = 0
        for i in range(self.len):
            total += w[i]/weightSum
            self.prefixSum.append(total)
    def pickIndex(self) -> int:
        rand = random.uniform(0, 1)
        index = bisect.bisect_left(self.prefixSum, rand)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
