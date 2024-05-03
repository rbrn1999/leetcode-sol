# link: https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

class Solution:
    def subsequenceSumOr(self, nums: list[int]) -> int:
        total = sum(nums)
        e = 0
        while total > 0:
            e += 1
            total >>= 1

        bits = [0] * e

        for num in nums:
            e = 0
            while num > 0:
                bits[e] += num % 2
                num >>= 1
                e += 1

        result = 0
        for e in range(len(bits)):
            if e < len(bits)-1:
                bits[e+1] += bits[e] // 2
            if bits[e] > 0:
                result |= 1 << e

        return result

class Solution:
    def subsequenceSumOr(self, nums: list[int]) -> int:
        result = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            result |= num
            result |= prefix_sum

        return result
