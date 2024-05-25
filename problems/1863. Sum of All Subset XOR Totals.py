# link: https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# backtracking
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def helper(i: int, val: int) -> int:
            if i == len(nums):
                return 0

            return helper(i+1, val) + (val ^ nums[i]) + helper(i+1, val^nums[i])
        
        return helper(0, 0)
    
# math, bit manipulation
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        # if there's a bit in any position, half of the subsets would have the bit, and the other half wouldn't
        # '0', '1' -> ('1', '0')
        # '0', '1', '1' -> ('1', '0'), '1', '0'
        # '0', '1', '1', '0' -> [('1', '0'), '1', '0'], [('1', '0'), '1', '0'] 
        # ...
        bits = 0
        for num in nums:
            bits |= num
        
        return bits * (2 ** (len(nums)-1))
