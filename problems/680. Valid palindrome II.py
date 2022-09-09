# link: https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.



# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            if s[i] == s[-1-i]:
                continue
            return (s[i+1:n//2 + n%2] ==s[n//2+1:n-i][::-1] or s[i:n//2-((n-1)%2)] == s[n//2:-i-1][::-1])
        return True