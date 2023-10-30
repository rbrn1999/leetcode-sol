# link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def countBits(num):
            bits = 0
            while num > 0:
                bits += num & 1
                num >>= 1
            return bits
        return sorted(arr, key=lambda x: (countBits(x), x))

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))