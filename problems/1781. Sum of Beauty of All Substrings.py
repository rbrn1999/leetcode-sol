# link: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution:
    def beautySum(self, s: str) -> int:
        result = 0

        for l in range(len(s)):
            freq = {}
            for r in range(l, len(s)):
                freq[s[r]] = freq.get(s[r], 0) + 1
                result += max(freq.values()) - min(freq.values())
        
        return result