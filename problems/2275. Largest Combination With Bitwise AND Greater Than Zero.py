# link: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

import math
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        n = int(math.log(max(candidates), 2))
        answer = 0
        for i in range(n+1):
            count = 0
            mask = 2 ** i
            for c in candidates:
                if c & mask:
                    count += 1
            answer = max(answer, count)

        return answer