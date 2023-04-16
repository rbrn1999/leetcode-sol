# link: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

from collections import defaultdict
from functools import cache
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        position_char_counts = defaultdict(lambda: defaultdict(int)) # {index: {char: count}}
        for word in words:
            for i in range(len(word)):
                position_char_counts[i][word[i]] += 1

        @cache
        def helper(start_index: int=0, target_index: int=0) -> int:
            if target_index == len(target):
                return 1
            if start_index == len(words[0]):
                return 0

            count = 0
            char = target[target_index]
            for i in range(start_index, len(words[0]) - (len(target) - (target_index+1))):
                count += position_char_counts[i][char] * helper(i+1, target_index+1) % int(1E9 + 7)
            return count % int(1E9 + 7)

        return helper()

