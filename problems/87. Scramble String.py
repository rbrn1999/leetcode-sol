# link: https://leetcode.com/problems/scramble-string/

from functools import cache
from collections import Counter
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        for i in range(1, len(s1)):
            s1_left, s1_right = s1[:i], s1[i:]
            s1_left_count = Counter(s1_left)
            s1_right_count = Counter(s1_right)
            s2_left, s2_right = s2[:i], s2[i:]
            s2_left_count = Counter(s2_left)
            s2_right_count = Counter(s2_right)
            if s1_left_count == s2_left_count and s1_right_count == s2_right_count and self.isScramble(s1_left, s2_left) and self.isScramble(s1_right, s2_right):
                return True
            s2_left, s2_right = s2[:len(s2)-i], s2[len(s2)-i:]
            s2_left_count = Counter(s2_left)
            s2_right_count = Counter(s2_right)
            if s1_left_count == s2_right_count and s1_right_count == s2_left_count and self.isScramble(s1_left, s2_right) and self.isScramble(s1_right, s2_left):
                return True

        return False
