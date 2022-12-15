# link: https://leetcode.com/problems/longest-square-streak-in-an-array/

from collections import deque
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        memo = deque()
        result = -1
        for num in nums:
            insertFlag = False
            for _ in range(len(memo)):
                square, length = memo.popleft()
                if square == num:
                    memo.append([num ** 2, length + 1])
                    insertFlag = True
                    break
                elif square > num:
                    memo.appendleft([square, length])
                    break
                else:
                    result = max(result, length)

            if not insertFlag:
                memo.append([num ** 2, 1])

        for _, length in memo:
            result = max(result, length)

        return result if result >= 2 else -1

