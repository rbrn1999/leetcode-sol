# link: https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

from collections import defaultdict
class Solution:
    def medianOfUniquenessArray(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n+1) // 2

        def atMost(k: int) -> int: # subarray count with at most k distinct numbers
            count = 0
            freq = defaultdict(int)
            l = 0
            for r in range(n):
                freq[nums[r]] += 1
                while len(freq) > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += r-l+1

            return count

        # binary search
        low = 1
        high = len(set(nums))
        while low < high:
            k = (low + high) // 2
            if atMost(k) >= (total // 2 + total % 2):
                high = k
            else:
                low = k + 1

        return low
