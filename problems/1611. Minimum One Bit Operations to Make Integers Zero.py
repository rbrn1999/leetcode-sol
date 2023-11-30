# link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

# Approach 1
import math
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 2^k -> 0: (2^k + 2^(k-1) + ... + 2^0) = 2^(k+1) - 1
        def helper(n, k):
            if k < 0: # n == 0 works, too
                return 0
            if 2 ** k & n > 0:
                return (2 ** (k+1) - 1) - helper(n ^ (2 ** k), k-1)
            else:
                return helper(n, k-1)
        
        k = int(math.log(n, 2)) if n > 0 else -1
        return helper(n, k)
    
# Approach 2
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 2^k -> 0: (2^k + 2^(k-1) + ... + 2^0) = 2^(k+1) - 1
        if n == 0:
            return 0
        k = 0
        while 2 ** (k+1) <= n:
            k += 1

        return (2 ** (k+1) - 1) - self.minimumOneBitOperations(n ^ (2 ** k))
        