# link: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        char_count = {}
        result = 0
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            while len(char_count) > 2:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1
            result = max(result, r-l+1)
        
        return result
            