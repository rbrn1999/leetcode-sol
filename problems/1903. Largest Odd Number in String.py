# link: https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        end = len(num)
        while end-1 >= 0 and int(num[end-1]) % 2 == 0:
            end -= 1
        return num[:end]