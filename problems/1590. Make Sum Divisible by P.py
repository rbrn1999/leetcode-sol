# link: https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        result = len(nums)
        remain_index = {0: -1}
        r = 0
        for i, num in enumerate(nums):
            r = (r + num) % p
            remain_index[r] = i
            if (r-target+p)%p in remain_index:
                j = remain_index[(r-target+p)%p]
                result = min(result, i-j)

        return result if result < len(nums) else -1
