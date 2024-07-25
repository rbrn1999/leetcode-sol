# link: https://leetcode.com/problems/sort-array-by-increasing-frequency/

from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        num_count_dict = Counter(nums)
        num_count_list = [(num, count) for num, count in num_count_dict.items()]
        num_count_list.sort(key=lambda x: (x[1], -x[0]))
        result = []
        for num, count in num_count_list:
            result.extend([num] * count)

        return result
