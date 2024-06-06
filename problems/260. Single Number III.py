# link: https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0 # will get a xor b
        for num in nums:
            xor ^= num

        bit = 1
        # find a bit that's different between a and b
        while bit & xor == 0:
            bit <<= 1


        # divide the numbers into 2 groups based on whether they have the bit
        # the same numbers will be grouped into the same group
        # xor all the numbers in the group and the numbers that appears twice will be cancelled out
        # a and b will be in different groups
        with_bit_xor = 0
        without_bit_xor = 0

        for num in nums:
            if num & bit:
                with_bit_xor ^= num
            else:
                without_bit_xor ^= num

        return [with_bit_xor, without_bit_xor]
