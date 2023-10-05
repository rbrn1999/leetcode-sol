# link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        l = 0
        while l < len(arr):
            if s[l] == ' ':
                l += 1
                continue
            r = l + 1
            while r < len(s) and s[r] != ' ':
                r += 1
            p = r
            r -= 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            l = p
        
        return ''.join(arr)
