# link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1            
            nonlocal res
            if r - l > len(res):
                res = s[l:r]
        
        for i in range(len(s)):
            if len(res) / 2 > min((len(s)-i) , i+1):
                break
            helper(i, i)
            helper(i, i+1)
        
        return res

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         def palindrome(mid): # will consider odd and even length string eg. "abc", "abbc"
#             l = r = mid
#             while l >= 0 and r < n and s[l] == s[r]:
#                 l-= 1
#                 r += 1
#             range1 = l+1, r
#             l, r= mid-1, mid
#             while l >= 0 and r < n and s[l] == s[r]:
#                 l-= 1
#                 r += 1
#             range2 = l+1, r
#             if range1[1]- range1[0] > range2[1]- range2[0]:
#                 return ((range1[1]-range1[0]+1) , range1)
#             else:
#                 return ((range2[1]-range2[0]+1) , range2)
            
#         longest = 0
#         longestRange = (0, 0)
#         for i in range(n):
#             length, (newRange) = palindrome(i)
#             if  length > longest:
#                 longest = length
#                 longestRange = newRange
        
#         return s[longestRange[0]:longestRange[1]]