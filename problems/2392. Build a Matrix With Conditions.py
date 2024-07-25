# link: https://leetcode.com/problems/build-a-matrix-with-conditions/

from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        m, n = len(rowConditions), len(colConditions)
        matrix = [[0] * k for _ in range(k)]
        coordinates = [[-1, -1] for _ in range(k)] # coordinates[num-1] -> coordinate for value "num"

        # top-sort for row
        indegree = [0] * k
        belows = [list() for _ in range(k)]
        for above, below in rowConditions:
            indegree[below-1] += 1
            belows[above-1].append(below-1)

        q = deque(i for i in range(k) if indegree[i] == 0)
        rowOrder = []

        while q:
            num = q.popleft()
            rowOrder.append(num)
            for below in belows[num]:
                indegree[below] -= 1
                if indegree[below] == 0:
                    q.append(below)

        if any(indegree[i] > 0 for i in range(k)):
            return []

        # top-sort for col
        indegree = [0] * k
        rights = [list() for _ in range(k)]
        for left, right in colConditions:
            indegree[right-1] += 1
            rights[left-1].append(right-1)

        q = deque(i for i in range(k) if indegree[i] == 0)
        colOrder = []

        while q:
            num = q.popleft()
            colOrder.append(num)
            for right in rights[num]:
                indegree[right] -= 1
                if indegree[right] == 0:
                    q.append(right)

        if any(indegree[i] > 0 for i in range(k)):
            return []

        for i in range(k):
            coordinates[rowOrder[i]][0] = i
            coordinates[colOrder[i]][1] = i

        for i, (row, col) in enumerate(coordinates):
            # convert back to 1-index
            matrix[row][col] = i+1

        return matrix
