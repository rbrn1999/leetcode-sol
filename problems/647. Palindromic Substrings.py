# link: https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(start, end): # calculate Palindromic substrings expanded from a given center 
            count = 0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                count += 1
                start -= 1
                end += 1
            return count
            
        
        # count = 0
        # for i in range(len(s)):
        #     count += helper(i, i)
        #     count += helper(i, i+1)
        # return count
        return sum(helper(i, i) + helper(i, i+1) for i in range(len(s)))