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

# Sliding Window

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        result = 0
        for uniqueCount in range(1, len(set(s)) + 1):
            l, r = 0, 0
            freq = {}
            atLeastK = 0

            while r < len(s):
                if len(freq) <= uniqueCount: # try to expand window
                    freq[s[r]] = freq.get(s[r], 0) + 1
                    if freq[s[r]] == k:
                        atLeastK += 1

                    r += 1
                else: # shrink window
                    if freq[s[l]] == k:
                        atLeastK -= 1

                    freq[s[l]] -= 1
                    if freq[s[l]] == 0:
                        del freq[s[l]]

                    l += 1

                if atLeastK == uniqueCount and len(freq) == uniqueCount:
                    result = max(result, r-l)


        return result
