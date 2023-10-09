# link: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

import math
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = int(math.log(max(nums), 2))
        bit_count = [0] * (n+1)
        for num in nums:
            e = 0
            while num:
                bit_count[e] += num % 2
                num //= 2
                e += 1

        answer = 0
        for _ in range(k):
            num = 0
            for i in range(n+1):
                if bit_count[i] > 0:
                    num += 2 ** i
                    bit_count[i] -= 1
            answer += num ** 2
            answer %= (10 ** 9 + 7)
        
        return answer