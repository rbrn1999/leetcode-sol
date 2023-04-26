#link: https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        # if num == 0:
        #     return 0
        # elif num % 9 == 0:
        #     return 9
        # else:
        #     return num % 9

        # one-liner
        return 1 + (num-1) % 9 if num else 0

