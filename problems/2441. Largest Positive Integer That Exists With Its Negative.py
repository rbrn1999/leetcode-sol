# link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        seen = set()
        answer = -1
        for num in nums:
            if -num in seen:
                answer = max(answer, abs(num))

            seen.add(num)
        
        return answer