# link: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
            return [num // 3 - 1, num // 3, num // 3 + 1] if num % 3 == 0 else []
