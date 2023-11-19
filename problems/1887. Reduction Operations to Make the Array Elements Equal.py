# link: https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ops = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # reduce all seen numbers (all equal to nums[i-1]) to nums[i]
                ops += i
        
        return ops