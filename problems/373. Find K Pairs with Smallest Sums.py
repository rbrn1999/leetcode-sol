# link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        heap = [(nums1[0]+nums2[0], 0, 0)]
        result = []
        visited = set((0, 0))
        for _ in range(min(k, m*n)):
            val, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if i+1 < m and j < n and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if i < m and j+1 < n and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))

        return result

