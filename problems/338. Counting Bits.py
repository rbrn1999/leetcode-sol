# link: https://leetcode.com/problems/counting-bits/

import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        exp = math.ceil(math.log(n, 2))
        res = [0]
        for i in range(0, exp+1):
            res.extend([1+n for n in res])
        return res[:n+1]
