# link: https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i = j = k
        val = nums[k]
        score = 0
        while i >= 0 and j < n:
            # not necessary
            while i-1 >= 0 and nums[i-1] >= val:
                i -= 1
            while j+1 < n and nums[j+1] >= val:
                j += 1
                
            score = max(score, (j-i+1) * val)

            if (nums[i-1] if i > 0 else 0) < (nums[j+1] if j < n-1 else 0):
                j += 1
                val = min(val, nums[j])
            else:
                i -= 1
                val = min(val, nums[i])
        
        return score