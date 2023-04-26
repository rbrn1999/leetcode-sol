# link: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

import math
from collections import Counter
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n - Counter(nums)[1]

        minLength = float('inf')
        for start in range(n):
            gcd = nums[start]
            for end in range(start, min(start+minLength, n)):
                gcd = math.gcd(gcd, nums[end])
                if gcd == 1:
                    minLength = min(minLength, end-start+1)
                    break

        return n + minLength - 2 if minLength != float('inf') else -1

