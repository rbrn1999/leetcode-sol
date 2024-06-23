# link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# 2 Deques

from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_dq = deque() # decreasing order
        min_dq = deque() # increasing order
        max_length = 0

        l = 0
        for r, num in enumerate(nums):
            while max_dq and max_dq[-1] < num:
                max_dq.pop()
            max_dq.append(num)

            while min_dq and min_dq[-1] > num:
                min_dq.pop()
            min_dq.append(num)
            
            while max_dq[0] - min_dq[0] > limit:
                if max_dq[0] == nums[l]:
                    max_dq.popleft()
                if min_dq[0] == nums[l]:
                    min_dq.popleft()
                l += 1

            max_length = max(max_length, r-l+1)
        
        return max_length

# SortedList (tree set, multi set)
from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        length = 0
        l = 0
        sorted_window = SortedList()

        for r in range(len(nums)):
            sorted_window.add(nums[r])
            while sorted_window[-1] - sorted_window[0] > limit:
                sorted_window.remove(nums[l])
                l += 1

            length = max(length, r-l+1)

        return length

# 2 Heaps

import heapq
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        length = 0
        l = 0
        minHeap = []
        maxHeap = []

        for r in range(len(nums)):
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l = min(maxHeap[0][1], minHeap[0][1]) + 1
                # try to remove at least one of the min/max number
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)

            length = max(length, r-l+1)

        return length
