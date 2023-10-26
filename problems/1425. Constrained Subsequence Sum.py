# link: https://leetcode.com/problems/constrained-subsequence-sum/

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        q = deque() # monotonic decreasing queue; (val, i): max sum of subsequences ended at i
        ans = -float('inf')
        for i, num in enumerate(nums):
            val = num + (q[0][0] if q else 0)
            while q and val > q[-1][0]:
                q.pop()
            if val > 0:
                q.append((val, i))
            ans = max(ans, val)
            if i >= k and q and q[0][1] == i-k: # only keep element in range(i-k, i+k)
                q.popleft()

        return ans