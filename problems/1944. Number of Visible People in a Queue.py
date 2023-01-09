# link: https://leetcode.com/problems/number-of-visible-people-in-a-queue/

import bisect

class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        peopleSeen = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            higher = max(0, bisect.bisect_left(stack, -heights[i], key=lambda x: -x) - 1)
            peopleSeen[i] = len(stack) - higher
            while stack and stack[-1] < heights[i]:
                stack.pop()
            stack.append(heights[i])
        return peopleSeen