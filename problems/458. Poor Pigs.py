# link: https://leetcode.com/problems/poor-pigs/

import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = int(math.log(buckets, minutesToTest // minutesToDie + 1)) # can't use math.ceil because of floating point precision
        return pigs if (minutesToTest // minutesToDie + 1) ** pigs >= buckets else pigs + 1