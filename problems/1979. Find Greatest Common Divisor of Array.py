# link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = b = nums[0]
        for num in nums:
            a = min(a, num)
            b = max(b, num)

        while a > 0:
            a, b = b%a, a

        return b

