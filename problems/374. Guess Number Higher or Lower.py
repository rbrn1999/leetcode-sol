# link: https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        mid = (low + 1 + high) // 2
        while True:
            val = guess(mid)
            if val == 0:
                return mid
            elif val == -1:
                high = mid
                mid = (low + 1 + high) // 2
            else:
                low = mid
                mid = (low + high + 1) // 2

