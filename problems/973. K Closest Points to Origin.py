# link: https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda x, y: math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        result = []
        minheap = [(distance(x, y), x, y) for x, y in points]
        heapq.heapify(minheap)
        for _ in range(k):
            _, x, y = heapq.heappop(minheap)
            result.append([x, y])
        return result

