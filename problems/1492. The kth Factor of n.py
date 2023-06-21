# link: https://leetcode.com/problems/the-kth-factor-of-n/

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # 1st half
        for f in range(1, int(math.sqrt(n))+1):
            if n % f == 0:
                k -= 1
                if k == 0:
                    return f

        # 2nd half
        # don't include the mid point
        for i in range(math.ceil(math.sqrt(n))-1, 0, -1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i

        return -1

