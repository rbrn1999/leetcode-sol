# link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Divide and Conquer by removing invalid characters
from collections import Counter, deque
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        result = 0
        substrings = deque()
        substrings.append([0, len(s)-1])
        while substrings:
            l, r = substrings.popleft()
            char_count = Counter(s[l:r+1])
            invalid_char = set()
            for c in char_count:
                if char_count[c] < k:
                    invalid_char.add(c)

            if len(invalid_char) == 0:
                result = max(result, r-l+1)
                continue

            new_l = 0
            for new_r in range(l, r+1):
                if s[new_r] in invalid_char:
                    if new_r - 1 > new_l:
                        substrings.append([new_l, new_r-1])
                    new_l = new_r + 1

            if new_l < r:
                substrings.append([new_l, r])

        return result
