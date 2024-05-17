# link: https://leetcode.com/problems/reverse-pairs/

from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        seen = SortedList()
        total_pairs = 0 
        for num in reversed(nums):
            pair_count = seen.bisect_left(num)
            total_pairs += pair_count
            seen.add(num * 2)

        return total_pairs