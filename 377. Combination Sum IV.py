# link: https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target+1)

        for i in range(target+1):
            for num in nums:
                if num == i:
                    memo[i] += 1
                elif i-num > 0:
                    memo[i] += memo[i-num]

        return memo[-1]
