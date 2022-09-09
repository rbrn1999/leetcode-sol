# link: https://leetcode.com/problems/valid-anagram/

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(lambda: 0)
        t_dict = defaultdict(lambda: 0)
        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1

        return s_dict == t_dict
