# link: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = 0
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        max_freq = 1
        for i in range(len(nums)):
            low = 0
            high = i
            while low < high:
                mid = low + (high - low) // 2
                if prefix_sum[i] - prefix_sum[mid] + k >= nums[i] * (i-mid):
                    high = mid
                else:
                    low = mid + 1
            
            max_freq = max(i - low + 1, max_freq)
        
        return max_freq