# link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def palindrome(mid): # will consider odd and even length string eg. "abc", "abbc"
            l = r = mid
            while l >= 0 and r < n and s[l] == s[r]:
                l-= 1
                r += 1
            range1 = l+1, r
            l, r= mid-1, mid
            while l >= 0 and r < n and s[l] == s[r]:
                l-= 1
                r += 1
            range2 = l+1, r
            if range1[1]- range1[0] > range2[1]- range2[0]:
                return ((range1[1]-range1[0]+1) , range1)
            else:
                return ((range2[1]-range2[0]+1) , range2)
            
        longest = 0
        longestRange = (0, 0)
        for i in range(n):
            length, (newRange) = palindrome(i)
            if  length > longest:
                longest = length
                longestRange = newRange
        
        return s[longestRange[0]:longestRange[1]]