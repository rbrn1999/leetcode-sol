# link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cur = 0
        for num in nums:
            cur ^= num

        return (cur ^ k).bit_count()
