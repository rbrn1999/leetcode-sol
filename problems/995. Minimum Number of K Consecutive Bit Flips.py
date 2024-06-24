# link: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

# Queue
from collections import deque
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flips = 0
        state = 0 # 0: even flips, 1: odd flips
        q = deque()
        for i in range(n-k+1):
            if q and q[0] == i:
                q.popleft()
                state ^= 1
            nums[i] ^= state
            if nums[i] == 1:
                continue
            else:
                flips += 1
                state ^= 1
                q.append(i+k)
                nums[i] ^= 1

        for i in range(n-k+1, n):
            if q and q[0] == i:
                q.popleft()
                state ^= 1
            nums[i] ^= state

        return flips if all(num == 1 for num in nums) else -1

# Constant Space
class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flips = 0
        state = 0

        for i in range(n):
            if nums[i-k] == 2:
                state ^= 1

            if nums[i] ^ state == 1:
                continue
            else:
                if i > n-k:
                    return -1
                flips += 1
                state ^= 1
                nums[i] = 2

        return flips
