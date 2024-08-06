# link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(c for c in word)
        chars = list(char_count.keys())
        chars.sort(key=lambda c: char_count[c], reverse=True)
        cost = 1
        i = 0
        total_cost = 0
        for c in chars:
            total_cost += char_count[c] * cost

            i += 1
            if i == 8:
                i = 0
                cost += 1
        
        return total_cost