# link: https://leetcode.com/problems/diagonal-traverse-ii/

from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        diag_lists = defaultdict(list)
        for row in range(len(nums)-1, -1, -1):
            for col in range(len(nums[row])):
                diag_lists[row+col].append(nums[row][col])
        
        result = []
        for key in range(max(diag_lists.keys())+1):
            result.extend(diag_lists[key])
        
        return result

# BFS, More space efficient: O(n^(1/2))
from collections import deque
class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        q = deque([(0, 0)])
        result = []

        while q:
            i, j = q.popleft()
            result.append(nums[i][j])
            if i + 1 < len(nums) and j < len(nums[i+1]) and (not q or q[-1] != (i+1, j)):
                q.append((i+1, j))
            if j + 1 < len(nums[i]):
                q.append((i, j+1))
        
        return result