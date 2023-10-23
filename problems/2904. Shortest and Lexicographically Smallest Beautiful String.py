# link: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count = 0
        ans = ""
        l = 0
        for r in range(len(s)):
            if s[r] == '1':
                count += 1
            while l <= r and (count > k or s[l] != '1'):
                if s[l] == '1':
                    count -= 1
                l += 1
            if count == k:
                if ans == "" or r-l+1 < len(ans) or r-l+1 == len(ans) and s[l:r+1] < ans:
                    ans = s[l:r+1]
            
        
        return ans