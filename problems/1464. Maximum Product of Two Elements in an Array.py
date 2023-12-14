# link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

import heapq
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < 2:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)
        
        return (minHeap[0]-1) * (minHeap[1]-1)