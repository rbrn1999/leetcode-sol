# link: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        suffix_sum = sum(nums)
        prefix_sum = 0
        ans = []
        for i, num in enumerate(nums):
            left = num * i - prefix_sum
            right = suffix_sum - (len(nums)-i) * num
            ans.append(left+right)
            prefix_sum += num
            suffix_sum -= num
        
        return ans