# link: https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start: int, end: int) -> int:
            if start > end:
                return -1
            midIndex = (start + end) // 2
            if nums[midIndex] > target:
                return binarySearch(start, midIndex-1)
            elif nums[midIndex] < target:
                return binarySearch(midIndex+1, end)
            else:
                return midIndex
        return binarySearch(0, len(nums)-1)

output = Solution().search(nums = [2], target = 2)
print(output)