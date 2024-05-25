# link: https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = [] # monotonic decreasing stack
        nums1_index = {val: i for i, val in enumerate(nums1)}
        result = [-1] * len(nums1)
        for num2 in nums2:
            while stack and stack[-1] < num2:
                num1 = stack.pop()
                result[nums1_index[num1]] = num2
            
            if num2 in nums1_index:
                stack.append(num2)
        
        return result