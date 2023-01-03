# link: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        total = 0
        for i in range(n):
            total += nums[i]
            prefixSum[i] = total

        for i in range(n):
            left = prefixSum[i-1] if i > 0 else 0
            right = prefixSum[n-1] - prefixSum[i]
            if left == right:
                return i

        return -1
