# link: https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        prev = -float('inf')
        length = 0
        for left, right in pairs:
            if left > prev:
                length += 1
                prev = right
        
        return length