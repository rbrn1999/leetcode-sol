# link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            l = 0
            r = len(word)-1
            while l < r and word[l] == word[r]:
                l += 1
                r -= 1
            if l >= r:
                return word
        
        return ""