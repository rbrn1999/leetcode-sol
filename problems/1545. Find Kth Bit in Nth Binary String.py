# link: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

# Recursion
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        length = (1 << n) - 1

        if k < length // 2 + 1:
            return self.findKthBit(n-1, k)
        elif k == length // 2 + 1:
            return '1'
        else:
            return '1' if self.findKthBit(n-1, length+1-k) == '0' else '0'

# Iteration
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (1 << n) - 1
        invert = False
        while length > 1:
            half = length // 2 + 1
            if k == half:
                return '1' if not invert else '0'
            elif k < half:
                length = half - 1
            else:
                k = length + 1 - k
                length = half - 1
                invert = not invert

        return '0' if not invert else '1'
