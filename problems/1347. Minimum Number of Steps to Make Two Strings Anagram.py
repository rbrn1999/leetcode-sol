# link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

from collections import Counter
import string
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        diff = 0
        for c in string.ascii_lowercase:
            diff += abs(count_s[c] - count_t[c])
        
        return diff // 2