# link: https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modGroup = defaultdict(lambda: 0)
        result = 0
        offset = 0 # prefix sum
        for num in nums:
            num %= k
            offset = (offset + num) % k
            # new sequence start with the current number doesn't have offset (prefix sum)
            # (num - offset): cancel out the offset
            modGroup[(num - offset) % k] += 1
            result += modGroup[(k-offset) % k]

        return result

