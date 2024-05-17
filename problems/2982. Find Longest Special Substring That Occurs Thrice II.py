# link: https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        freq = defaultdict(list) # {char: list[int]} freq[char][i]: occurance of char * (i+1)

        prev = ''
        length = 0
        for c in s:
            if c == prev:
                length += 1
            else:
                prev = c
                length = 1

            if len(freq[c]) == length-1:
                freq[c].append(0)
            freq[c][length-1] += 1

        max_length = -1
        for c in freq:
            actul_freq = 0
            for i in range(len(freq[c])-1, -1, -1):
                actul_freq += freq[c][i]
                if actul_freq >= 3:
                    max_length = max(max_length, i+1)
                    break
        
        return max_length