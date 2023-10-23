# link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        r = 0
        duplicates = 0
        min_cost = n - 1
        for l in range(n):
            while r < n and nums[r] <= nums[l] + n-1:
                if r > 0 and nums[r] == nums[r-1]:
                    duplicates += 1
                r += 1
            cost = n - (r - l) + duplicates
            min_cost = min(min_cost, cost)
            if l < n-1 and nums[l] == nums[l+1]:
                duplicates -= 1
        
        return min_cost


# Remove Duplicates First
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        r = 0
        min_cost = n - 1
        for l in range(len(nums)):
            while r < len(nums) and nums[r] <= nums[l] + n-1:
                r += 1
            cost = n - (r - l)
            min_cost = min(min_cost, cost)
        
        return min_cost