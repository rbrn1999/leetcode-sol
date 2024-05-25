# link: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

from collections import deque
class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        q = deque() # (index of start of the subarray, prefixSum of the subarray) # value should be accending
        q.append((-1, 0))
        prefixSum = [nums[0]]
        for num in nums[1:]:
            prefixSum.append(num + prefixSum[-1])
        
        answer = len(nums)+1
        for i, val in enumerate(prefixSum):
            while q and val - q[0][1] >= k:
                length = i - q.popleft()[0]
                answer = min(answer, length)
            while q and val <= q[-1][1]:
                q.pop()
            
            q.append((i, val))
        
        return answer if answer <  len(nums) + 1 else -1