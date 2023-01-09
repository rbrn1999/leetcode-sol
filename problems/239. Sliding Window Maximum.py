# link: https://leetcode.com/problems/sliding-window-maximum/

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(maxHeap)
        maxWindowArr = [-maxHeap[0][0]]
        for r in range(k, len(nums)):
            l = r - k + 1
            heapq.heappush(maxHeap, (-nums[r], r))
            while maxHeap[0][1] < l:
                heapq.heappop(maxHeap)
            maxWindowArr.append(-maxHeap[0][0])

        return maxWindowArr

