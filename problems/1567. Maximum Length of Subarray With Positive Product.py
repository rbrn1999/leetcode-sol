#link: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        answer = 0
        start = 0
        firstNeg = float('inf')
        oddNegs = False
        for end, num in enumerate(nums):
            if num == 0:
                start = end+1
                firstNeg = float('inf')
                oddNegs = False
                continue
            if (num > 0) != (oddNegs): #(num > 0 and not oddNegs) or (num < 0 and oddNegs):
                answer = max(answer, end-start+1)
            else:
                answer = max(answer, end-firstNeg)

            if num < 0:
                oddNegs = not oddNegs
                firstNeg = min(firstNeg, end)

        return answer

