# link: https://leetcode.com/problems/odd-even-jump/

from functools import cache
from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)
        oddJumps = []
        index_values = SortedList([(num, i) for i, num in enumerate(arr)])
        for i, num in enumerate(arr):
            index_values.remove((num, i))
            j = index_values.bisect_left((num, i))
            if j == len(index_values):
                oddJumps.append(-1)
            else:
                oddJumps.append(index_values[j][1])

        evenJumps = []
        index_values = SortedList([(num, -i) for i, num in enumerate(arr)])
        for i, num in enumerate(arr):
            index_values.remove((num, -i))
            j = index_values.bisect_left((num, 0)) # 0 is for tie-breaker: get the smallest index possible
            if j < len(index_values) and index_values[j][0] == num:
                evenJumps.append(-index_values[j][1])
            elif j - 1 >= 0:
                evenJumps.append(-index_values[j-1][1])
            else:
                evenJumps.append(-1)


        @cache
        def dfs(i: int, isOdd: bool) -> bool:
            if i == len(arr)-1:
                return True

            jump_map = oddJumps if isOdd else evenJumps
            if jump_map[i] == -1:
                return False
            else:
                return dfs(jump_map[i], not isOdd)


        result = 0
        for i in range(len(arr)):
            if dfs(i, True):
                result += 1

        return result

# Stack

from functools import cache
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        oddJumps = [-1] * n # next index that has >= current value
        evenJumps = [-1] * n # next index that has <= current value

        stack = []
        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                oddJumps[stack.pop()] = i
            stack.append(i)

        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                evenJumps[stack.pop()] = i
            stack.append(i)

        @cache
        def dfs(i: int, isOdd: bool) -> bool:
            if i == len(arr)-1:
                return True

            jump_map = oddJumps if isOdd else evenJumps
            if jump_map[i] == -1:
                return False
            else:
                return dfs(jump_map[i], not isOdd)


        result = 0
        for i in range(len(arr)):
            if dfs(i, True):
                result += 1

        return result
