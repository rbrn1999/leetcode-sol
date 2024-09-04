# link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        result = 0
        for i, num in enumerate(arr):
            left_even = i // 2
            right_even = (n-1-i) // 2
            left_odd = (i+1) // 2
            right_odd = (n-i) // 2
            result += num * (((1 + left_even) * (1 + right_even)) + (left_odd * right_odd))
        
        return result
