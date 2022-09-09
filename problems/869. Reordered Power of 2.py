# link: https://leetcode.com/problems/reordered-power-of-2/

import math
from collections import defaultdict
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def match(d1, d2) -> True:
            for i in range(10):
                if d1[i] != d2[i]:
                    return False
            return True

        bottomPower = math.ceil(math.log(10**int(math.log(n, 10)), 2))
        topPower = int(math.log(10**(int(math.log(n, 10))+1), 2))
        target = defaultdict(lambda: 0)
        while n > 0:
            target[n%10] += 1
            n //= 10
        for i in range(bottomPower, topPower+1):
            d = defaultdict(lambda: 0)
            cur = 2**i
            while cur > 0:
                d[cur%10] += 1
                cur //= 10
            if match(d, target):
                return True

        return False
