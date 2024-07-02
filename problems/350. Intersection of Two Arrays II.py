# link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = defaultdict(int)
        for num in nums1:
            freq[num] += 1

        result = []
        for num in nums2:
            if freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result
