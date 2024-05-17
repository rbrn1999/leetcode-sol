# link: 

class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        max_jumps = [0] + [-1] * (n-1)

        for i in range(n-1):
            if max_jumps[i] == -1:
                continue
            for j in range(i+1, n):
                if nums[j] - nums[i] <= target and nums[j] - nums[i] >= -target:
                    max_jumps[j] = max(max_jumps[j], max_jumps[i] + 1)
        
        return max_jumps[-1]