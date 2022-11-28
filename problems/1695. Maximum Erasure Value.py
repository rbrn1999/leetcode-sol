# link: https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        accuDp = [0] # i: sum(nums[:i])
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            accuDp.append(curSum)
        
        score = 0
        start = 0
        
        for end in range(1, len(nums)):
            duplicate = nums[start:end+1].index(nums[end]) + start
            if duplicate != end:
                score = max(score, accuDp[end] - accuDp[start])
                start = duplicate + 1
                
        score = max(score, accuDp[-1] - accuDp[start])
        return score
