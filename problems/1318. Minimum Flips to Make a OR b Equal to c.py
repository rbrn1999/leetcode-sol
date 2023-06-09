# link: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

# Bit Manipulation
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip_count = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a % 2, b % 2, c % 2
            a, b, c = a // 2, b // 2, c // 2
            if bit_a | bit_b == bit_c:
                pass
            elif bit_c == 1:
                flip_count += 1
            else:
                flip_count += int(bit_a) + int(bit_b)
        
        return flip_count

# Count the Number of Set Bits Using Built-in Function
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # Python >= 3.10
        return ((a | b) ^ c).bit_count() + (a & b & ((a | b) ^ c)).bit_count()
        # Python < 3.10
        return bin((a | b) ^ c).count("1") + bin(a & b & ((a | b) ^ c)).count("1")