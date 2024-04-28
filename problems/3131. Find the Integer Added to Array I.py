# link: https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        num1 = min(nums1)
        num2 = min(nums2)
        return num2 - num1
