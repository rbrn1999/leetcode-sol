# link: https://leetcode.com/problems/largest-number/

import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def comp(lhs: str, rhs: str) -> int:
            if (lhs + rhs) > (rhs + lhs):
                return 1
            elif (lhs + rhs) < (rhs + lhs):
                return -1
            else:
                return 0

        nums_str = [str(num) for num in nums]
        nums_str.sort(key=functools.cmp_to_key(comp), reverse=True)
        result = ''.join(nums_str)
        i = 0
        while result[i] == '0' and i < len(result)-1:
            i += 1

        return result[i:]
