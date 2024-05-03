# link: https://leetcode.com/problems/number-of-wonderful-substrings/

from collections import defaultdict
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        answer = 0
        bit_mask_freq = defaultdict(int)
        bit_mask = 0
        bit_mask_freq[0] = 1
        for i in range(len(word)):
            bit = 1 << (ord(word[i])-ord('a'))
            bit_mask ^= bit
            answer += bit_mask_freq[bit_mask]
            for j in range(10):
                answer += bit_mask_freq[bit_mask ^ (1 << j)]

            bit_mask_freq[bit_mask] += 1


        return answer
