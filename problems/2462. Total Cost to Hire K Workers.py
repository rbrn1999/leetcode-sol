# link: https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        head = costs[:candidates]
        tail = costs[max(candidates, len(costs)-candidates):]
        left = candidates
        right = len(costs)-candidates-1

        heapq.heapify(head)
        heapq.heapify(tail)

        total_cost = 0
        for _ in range(k):
            if head and (not tail or head[0] <= tail[0]):
                total_cost += heapq.heappop(head)
                if left <= right:
                    heapq.heappush(head, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(tail)
                if left <= right:
                    heapq.heappush(tail, costs[right])
                    right -= 1
        
        return total_cost