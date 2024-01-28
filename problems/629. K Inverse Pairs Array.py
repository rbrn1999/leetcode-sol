# link: https://leetcode.com/problems/k-inverse-pairs-array/

from functools import cache
class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        if n == 0:
            return 0
        # count = 0
        # for i in range(min(k+1, n)):
        #     count = (count + self.kInversePairs(n-1, k-i)) % (10 ** 9 + 7)
        count = self.kInversePairs(n-1, k) + self.kInversePairs(n, k-1) - (self.kInversePairs(n-1, k-n) if n <= k else 0)
        count %= (10 ** 9 + 7)
        
        return count