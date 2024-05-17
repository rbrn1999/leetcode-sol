# link: https://leetcode.com/problems/longest-palindrome/

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        hasExtra = False

        length = 0
        for count in char_count.values():
            if count % 2 == 1:
                hasExtra = True

            length += count - (count % 2)
        
        return length + int(hasExtra)