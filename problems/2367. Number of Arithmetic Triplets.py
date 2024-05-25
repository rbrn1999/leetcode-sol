# link: https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        seen = set()
        result = 0
        for i, num in enumerate(nums):
            if num - diff in seen and num - diff * 2 in seen:
                result += 1
            seen.add(num)
        
        return result