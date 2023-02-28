# link: https://leetcode.com/problems/construct-quad-tree/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def __construct(row, col, length):
            val = grid[row][col]
            isLeaf = True
            for i in range(row, row+length):
                for j in range(col, col+length):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
            if isLeaf:
                return Node(val, isLeaf, None, None, None, None)
            offset = length // 2
            topLeft = __construct(row, col, offset)
            topRight = __construct(row, col + offset, offset)
            bottomLeft = __construct(row + offset, col, offset)
            bottomRight = __construct(row + offset, col + offset, offset)
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        return __construct(0, 0, len(grid))
