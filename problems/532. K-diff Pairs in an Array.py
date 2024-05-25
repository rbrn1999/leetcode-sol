# link: https://leetcode.com/problems/k-diff-pairs-in-an-array/

from collections import Counter
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        num_freq = Counter(nums)
        result = 0
        for num in num_freq:
            if k == 0:
                result += int(num_freq[num] >= 2)
            else:
                result += int(num - k in num_freq)
        
        return result