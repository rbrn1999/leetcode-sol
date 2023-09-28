# link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        
        dp = set() # sums of combinations
        dp.add(0)
        for num in nums:
            if target-num in dp:
                return True
            next_dp = dp.copy()
            for prev in dp:
                next_dp.add(prev + num)
            dp = next_dp
                
        return False