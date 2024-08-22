# link: https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        result = 0
        e = 0
        while num > 0:
            result += ((num+1)%2) << e
            num >>= 1
            e += 1
        
        return result

class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ ((1 << num.bit_length()) - 1)