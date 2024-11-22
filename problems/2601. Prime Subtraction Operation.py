# link: https://leetcode.com/problems/prime-subtraction-operation/

import math
from functools import cache
class Solution:
    @cache
    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False

        return True

    def primeSubOperation(self, nums: list[int]) -> bool:
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            for p in range(min(nums[i], nums[i]-nums[i-1]-1), 1, -1):
                if self.isPrime(p):
                    nums[i] -= p
                    break

            if nums[i] <= nums[i-1]:
                return False

        return True
