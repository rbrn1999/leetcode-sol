# link: https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Time Complexity O(n^3): pass
# but could be solved in O(n)...
class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums)-1):
                if nums[i] == nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[k] != nums[i] and nums[k] != nums[j]:
                        count += 1
        
        return count