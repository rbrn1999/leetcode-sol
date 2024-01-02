# link: https://leetcode.com/problems/assign-cookies/

import heapq
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)
        
        content_count = 0

        while s and g:
            cookie_size = heapq.heappop(s)
            if cookie_size >= g[0]:
                heapq.heappop(g)
                content_count += 1
        
        return content_count