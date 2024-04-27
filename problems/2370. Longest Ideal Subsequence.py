# link: https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        char_length = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            char_length[i] = max(char_length[max(0, i-k): min(26, i+k+1)]) + 1
        
        return max(char_length)