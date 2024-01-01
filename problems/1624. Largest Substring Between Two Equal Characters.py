# link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/

# Array
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        low_high = [[-1, -1] for _ in range(26)]

        for i in range(len(s)):
            if low_high[ord(s[i]) - ord('a')][0] == -1:
                low_high[ord(s[i]) - ord('a')][0] = i
            else:
                low_high[ord(s[i]) - ord('a')][1] = i

        return max(high-low-1 for low, high in low_high)

# Hash Map
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        last = {}
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            else:
                last[s[i]] = i
        
        result = -1
        for c in first:
            if c in last:
                result = max(result, last[c] - first[c] - 1)
        
        return result