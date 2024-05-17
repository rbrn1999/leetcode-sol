# link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        seen = SortedList()
        result = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            smaller_count = seen.bisect_left(nums[i])
            result[i] = smaller_count
            seen.add(nums[i])

        return result
