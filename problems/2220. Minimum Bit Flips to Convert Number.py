# link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        while start > 0 or goal > 0:
            flips += (start & 1) ^ (goal & 1)
            start >>= 1
            goal >>= 1

        return flips
