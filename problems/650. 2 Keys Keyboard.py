# link: https://leetcode.com/problems/2-keys-keyboard/


# Recursion
import sys
class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def helper(char_count: int = 1, clipboard: int = 0) -> int:
            if char_count == n:
                return 0
            if char_count > n:
                return sys.maxsize

            if (char_count, clipboard) in cache:
                return cache[(char_count, clipboard)]

            # copy and paste
            steps = 2 + helper(char_count * 2, char_count)
            # only paste
            if clipboard > 0:
                steps = min(steps, 1 + helper(char_count + clipboard, clipboard))

            cache[(char_count, clipboard)] = steps
            return steps

        return helper()


# Math
