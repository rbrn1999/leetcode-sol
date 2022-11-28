# link: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

from typing import List
from bisect import insort
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        valid = 0
        left = 0
        right = []
        for i, flip in enumerate(flips):
            if right and right[0] == i:
                left += 1
                right.pop(0)

            if flip - 1 > i:
                insort(right, flip-1)
            else:
                left += 1
                if left == i+1:
                    valid += 1
        return valid
