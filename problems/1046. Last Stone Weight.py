# link: https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while heap:
            y = -heapq.heappop(heap)
            if not heap:
                return y
            x = -heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -(y - x))

        return 0


