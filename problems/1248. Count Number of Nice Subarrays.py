# link: https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_odds = [0]
        for num in nums:
            prefix_odds.append(prefix_odds[-1] + num % 2)
        
        result = 0
        odd_freq_count = {}

        for prefix_odd in prefix_odds:
            if prefix_odd - k in odd_freq_count:
                result += odd_freq_count.get(prefix_odd - k)
            
            odd_freq_count[prefix_odd] = odd_freq_count.get(prefix_odd, 0) + 1
        
        return result