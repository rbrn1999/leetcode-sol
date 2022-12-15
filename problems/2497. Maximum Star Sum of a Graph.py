from collections import defaultdict
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        edges_d = defaultdict(list)
        n = len(vals)
        for a, b in edges:
            edges_d[a].append(b)
            edges_d[b].append(a)

        maxSum = -float('inf')

        for mid in range(n):
            curSum = vals[mid]
            curSum += sum(sorted([vals[i] for i in edges_d[mid] if vals[i] > 0], reverse=True)[:k])
            maxSum = max(maxSum, curSum)

        return maxSum
