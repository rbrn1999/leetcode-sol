# link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq
class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(heap)
        min_range = [-2 * 10 ** 5, 2 * 10 ** 5]
        cur_max = max(heap[i][0] for i in range(len(heap)))

        while len(heap) == len(nums):
            cur_min, i, j = heapq.heappop(heap)

            if cur_max - cur_min < min_range[1] - min_range[0]:
                min_range = [cur_min, cur_max]

            if j + 1 < len(nums[i]):
                cur_max = max(cur_max, nums[i][j+1])
                heapq.heappush(heap, (nums[i][j+1], i, j+1))

        return min_range
