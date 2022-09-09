# link: https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq 

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for num in nums[k:]:
            heapq.heappush(pq, num)
            heapq.heappop(pq)
        return pq[0]
