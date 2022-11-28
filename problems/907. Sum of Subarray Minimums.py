# link: https://leetcode.com/problems/sum-of-subarray-minimums/
# soulution reference: https://leetcode.com/problems/sum-of-subarray-minimums/solution/

# Monotonic Stack
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                minIndex = stack.pop()
                left_boundary = stack[-1] if stack else -1
                right_boundary = i

                subArrCount = (minIndex - left_boundary) * (right_boundary - minIndex)
                result += subArrCount * arr[minIndex]

            stack.append(i)

        return result % int(1E9 +7)
