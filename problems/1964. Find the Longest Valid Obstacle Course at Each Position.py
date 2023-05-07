
# Segment Tree: TLE
class SegmentTree:
    def __init__(self, L, R, total):
            self.left = None
            self.right = None
            self.L = L
            self.R = R
            self.max = total

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(L, R, nums[L])

        M = (L + R) // 2
        root = SegmentTree(L, R, 0)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M+1, R)
        root.max = max(root.left.max, root.right.max)
        return root

    def update(self, index, value):
        if self.L == self.R:
            self.max = value
            return
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, value)
        else:
            self.left.update(index, value)
        self.max = max(self.left.max, self.right.max)
    
    def rangeQuery(self, L, R):
        if L == self.L and R == self.R:
            return self.max
        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return max(self.left.rangeQuery(L, M), self.right.rangeQuery(M+1, R))
    
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        answer = []
        val_to_ind = {value: index for index, value in enumerate(sorted(set(obstacles)))}
        segmentTree = SegmentTree.build([0] * len(val_to_ind), 0, len(val_to_ind)-1)
        for obstacle in obstacles:
            prev_max = segmentTree.rangeQuery(0, val_to_ind[obstacle])
            segmentTree.update(val_to_ind[obstacle], prev_max + 1)
            answer.append(prev_max + 1)
        return answer

# DP + Binary Search
from bisect import bisect_right
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        n = len(obstacles)
        answer = []
        dp = [float('inf')] * (n+1) # dp[i], whiere i = length of non-decreasing sequence, is the smallest ending value

        for obstacle in obstacles:
            index = bisect_right(dp, obstacle)
            dp[index] = obstacle
            answer.append(index + 1)

        return answer

            