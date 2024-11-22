# link: https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        pattern_count = defaultdict(int)
        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 if num == 0 else 0 for num in row)
            pattern_count[pattern] += 1

        return max(pattern_count.values())
