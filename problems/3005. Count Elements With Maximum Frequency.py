# link: https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        maxFreq = max(count.values())

        result = 0
        for num in count:
            if count[num] == maxFreq:
                result += maxFreq
        
        return result
